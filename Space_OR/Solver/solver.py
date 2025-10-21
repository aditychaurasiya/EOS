import gurobipy as gp
from gurobipy import GRB


class Solver:
    def __init__(self, input_data):
        self.x = {}
        self.y = {}
        self.d = {}  # downlink amount variable
        self.m = {}  # memory variable
        self.p = {}  # power level variable
        self.vt_window = {}
        self.downlink_window = {}
        self.recharge_window = {}

        # Store input data
        self.downlink = input_data.downlink
        self.groundstation = input_data.groudstation
        self.statellite = input_data.statellite
        self.target = input_data.target
        self.vtw = input_data.vtw
        self.rechargewindow = input_data.rechargewindow
        self.input_data = input_data

        # Constants and Parameters
        self.zero = 0
        self.data_per_obs = 5  # GB of Observation data
        self.data_down = 10  # GB max that can be transfer to Ground station in one go
        self.max_per_day_obs = 5  # per day 5 obs can be made by satellite

        # Power parameters
        self.power_capacity = 100  # Wh max power capacity
        self.power_per_obs = 10  # Wh consumed per observation
        self.power_per_downlink = 5  # Wh consumed per GB downlinked
        self.charge_rate_per_slot = 15  # Wh recharged per time slot when in sunlight

        # Time Slots
        self.time_slots, self.dl_time_slots = input_data._create_time_slot_mapping()
        self.combined_slots = sorted(set(self.time_slots + self.dl_time_slots))

        # Build parameter dictionaries from input data
        self._build_vtw_parameters()
        self._build_downlink_parameters()
        self._build_recharge_parameters()

        # Env
        self.env = gp.Env()
        self.eos_model = gp.Model("Earth_Observation_Scheduling", env=self.env)

    def _build_vtw_parameters(self):
        """Build VTW binary parameters from input data"""
        for s in self.statellite:
            for t in self.target:
                for k in self.time_slots:
                    self.vt_window[s, t, k] = 0

        vtw_count = 0
        for vtw_obj in self.vtw.values():
            s = vtw_obj.satelliteid
            t = vtw_obj.target_id
            k = vtw_obj.timeSlotStart.strip()
            if s in self.statellite and t in self.target and k in self.time_slots:
                self.vt_window[s, t, k] = 1
                vtw_count += 1

        print(f"VTW Parameters: {vtw_count} windows enabled")

    def _build_downlink_parameters(self):
        """Build downlink window binary parameters from input data"""
        for s in self.statellite:
            for g in self.groundstation:
                for k in self.dl_time_slots:
                    self.downlink_window[s, g, k] = 0

        dl_count = 0
        for dl_obj in self.downlink.values():
            s = dl_obj.satelliteid
            g = dl_obj.groundstationid
            k = dl_obj.timeSlotStart.strip()

            if s in self.statellite and g in self.groundstation and k in self.dl_time_slots:
                self.downlink_window[s, g, k] = 1
                dl_count += 1

        print(f"Downlink Parameters: {dl_count} windows enabled")

    def _build_recharge_parameters(self):
        """Build recharge window binary parameters from input data"""
        # Initialize all to 0
        for s in self.statellite:
            for k in self.combined_slots:
                self.recharge_window[s, k] = 0

        # Set to 1 where recharge window exists
        recharge_count = 0
        for recharge_obj in self.rechargewindow.values():
            s = recharge_obj.satelliteid
            k = recharge_obj.timeSlotStart.strip()

            if s in self.statellite and k in self.combined_slots:
                self.recharge_window[s, k] = 1
                recharge_count += 1

        print(f"Recharge Parameters: {recharge_count} windows enabled\n")

    def run(self):
        self.create_decision_variables()
        self.create_constraints()
        self.create_objective()
        self.solve_mip()

    def create_decision_variables(self):
        # Decision variables for observations
        for s in self.statellite:
            for t in self.target:
                for k in self.time_slots:
                    self.x[s, t, k] = self.eos_model.addVar(
                        vtype=GRB.BINARY,
                        name=f"x_{s}_{t}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                    )

        # Decision variables for downlinks
        for s in self.statellite:
            for g in self.groundstation:
                for k in self.dl_time_slots:
                    self.y[s, g, k] = self.eos_model.addVar(
                        vtype=GRB.BINARY,
                        name=f"y_{s}_{g}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                    )

        # Decision variables for downlink amount
        for s in self.statellite:
            for g in self.groundstation:
                for k in self.dl_time_slots:
                    self.d[s, g, k] = self.eos_model.addVar(
                        vtype=GRB.CONTINUOUS,
                        lb=0,
                        ub=self.data_down,
                        name=f"d_{s}_{g}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                    )

        # Memory variables for all combined slots
        for s in self.statellite:
            for k in self.combined_slots:
                self.m[s, k] = self.eos_model.addVar(
                    vtype=GRB.CONTINUOUS,
                    lb=0,
                    name=f"m_{s}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                )

        # Power variables for all combined slots
        for s in self.statellite:
            for k in self.combined_slots:
                self.p[s, k] = self.eos_model.addVar(
                    vtype=GRB.CONTINUOUS,
                    lb=0,
                    ub=self.power_capacity,
                    name=f"p_{s}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                )

    def create_constraints(self):
        # 1. VTW constraint
        self.eos_model.addConstrs(
            (self.x[s, t, k] <= self.vt_window[s, t, k]
             for s in self.statellite
             for t in self.target
             for k in self.time_slots
             if (s, t, k) in self.x),
            name="vtw_constraint"
        )

        # 2. Observation limit per day
        for s in self.statellite:
            self.eos_model.addConstr(
                gp.quicksum(self.x[s, t, k]
                            for t in self.target
                            for k in self.time_slots
                            if (s, t, k) in self.x) <= self.max_per_day_obs,
                name=f"max_obs_per_day_{s}"
            )

        # 3. Single observation per target
        for t in self.target:
            obs_sum = gp.quicksum(self.x[s, t, k]
                                  for s in self.statellite
                                  for k in self.time_slots
                                  if (s, t, k) in self.x)
            self.eos_model.addConstr(obs_sum <= 1, name=f"single_obs_{t}")

        # 4. Memory balance over combined slots
        for s in self.statellite:
            for idx, k in enumerate(self.combined_slots):
                if idx == 0:
                    obs_in = gp.quicksum(
                        self.data_per_obs * self.x[s, t, k]
                        for t in self.target
                        if (s, t, k) in self.x
                    )
                    dl_out = gp.quicksum(
                        self.d[s, g, k]
                        for g in self.groundstation
                        if (s, g, k) in self.d
                    )
                    self.eos_model.addConstr(
                        self.m[s, k] == obs_in - dl_out,
                        name=f"mem_initial_{s}"
                    )
                else:
                    prev_k = self.combined_slots[idx - 1]
                    obs_in = gp.quicksum(
                        self.data_per_obs * self.x[s, t, k]
                        for t in self.target
                        if (s, t, k) in self.x
                    )
                    dl_out = gp.quicksum(
                        self.d[s, g, k]
                        for g in self.groundstation
                        if (s, g, k) in self.d
                    )
                    self.eos_model.addConstr(
                        self.m[s, k] == self.m[s, prev_k] + obs_in - dl_out,
                        name=f"memory_balance_{s}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                    )

        # 5. Memory capacity constraint
        for s in self.statellite:
            for k in self.combined_slots:
                self.eos_model.addConstr(
                    self.m[s, k] <= self.statellite[s].memory_capacity,
                    name=f"memory_capacity_{s}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                )

        # 6. Power balance over combined slots
        # Power at slot k = Power at slot (k-1) - power consumed + power recharged
        for s in self.statellite:
            for idx, k in enumerate(self.combined_slots):
                if idx == 0:
                    # Initial power level
                    power_consumed_obs = gp.quicksum(
                        self.power_per_obs * self.x[s, t, k]
                        for t in self.target
                        if (s, t, k) in self.x
                    )
                    power_consumed_dl = gp.quicksum(
                        self.power_per_downlink * self.d[s, g, k]
                        for g in self.groundstation
                        if (s, g, k) in self.d
                    )
                    power_recharged = self.charge_rate_per_slot * self.recharge_window.get((s, k), 0)

                    self.eos_model.addConstr(
                        self.p[s, k] == self.power_capacity - power_consumed_obs - power_consumed_dl + power_recharged,
                        name=f"power_initial_{s}"
                    )
                else:
                    prev_k = self.combined_slots[idx - 1]

                    power_consumed_obs = gp.quicksum(
                        self.power_per_obs * self.x[s, t, k]
                        for t in self.target
                        if (s, t, k) in self.x
                    )
                    power_consumed_dl = gp.quicksum(
                        self.power_per_downlink * self.d[s, g, k]
                        for g in self.groundstation
                        if (s, g, k) in self.d
                    )
                    power_recharged = self.charge_rate_per_slot * self.recharge_window.get((s, k), 0)

                    self.eos_model.addConstr(
                        self.p[s, k] == self.p[s, prev_k] - power_consumed_obs - power_consumed_dl + power_recharged,
                        name=f"power_balance_{s}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                    )

        # 7. Power capacity constraint
        for s in self.statellite:
            for k in self.combined_slots:
                self.eos_model.addConstr(
                    self.p[s, k] <= self.power_capacity,
                    name=f"power_capacity_upper_{s}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                )
                self.eos_model.addConstr(
                    self.p[s, k] >= 0,
                    name=f"power_capacity_lower_{s}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                )

        # 8. Downlink window constraint
        for s in self.statellite:
            for g in self.groundstation:
                for k in self.dl_time_slots:
                    if (s, g, k) in self.y:
                        self.eos_model.addConstr(
                            self.y[s, g, k] <= self.downlink_window[s, g, k],
                            name=f"downlink_window_{s}_{g}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                        )

        # 9. Link downlink amount to binary decision
        for s in self.statellite:
            for g in self.groundstation:
                for k in self.dl_time_slots:
                    if (s, g, k) in self.y and (s, g, k) in self.d:
                        self.eos_model.addConstr(
                            self.d[s, g, k] <= self.data_down * self.y[s, g, k],
                            name=f"link_downlink_amount_{s}_{g}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                        )

        # 10. Ground station conflict
        for g in self.groundstation:
            for k in self.dl_time_slots:
                self.eos_model.addConstr(
                    gp.quicksum(self.y[s, g, k]
                                for s in self.statellite
                                if (s, g, k) in self.y) <= 1,
                    name=f"groundstation_conflict_{g}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                )

        # 11. Satellite downlink exclusivity
        for s in self.statellite:
            for k in self.dl_time_slots:
                self.eos_model.addConstr(
                    gp.quicksum(self.y[s, g, k]
                                for g in self.groundstation
                                if (s, g, k) in self.y) <= 1,
                    name=f"satellite_downlink_exclusivity_{s}_{k.replace(':', '').replace('-', '_')}"
                )

    def create_objective(self):
        # Maximize observation value
        obs_value = gp.quicksum(
            self.target[t].urgency * self.target[t].importance * self.x[s, t, k]
            for s in self.statellite
            for t in self.target
            for k in self.time_slots
            if (s, t, k) in self.x
        )

        # Bonus for downlinks to ensure data transfer
        downlink_value = 0.1 * gp.quicksum(
            self.d[s, g, k]
            for s in self.statellite
            for g in self.groundstation
            for k in self.dl_time_slots
            if (s, g, k) in self.d
        )

        self.eos_model.setObjective(obs_value + downlink_value, GRB.MAXIMIZE)

    def solve_mip(self):
        self.eos_model.optimize()
        self.eos_model.write("eos.lp")

        if self.eos_model.status == GRB.INFEASIBLE:
            print("The model is infeasible.")
            self.eos_model.computeIIS()
            self.eos_model.write("model.ilp")

        elif self.eos_model.status == GRB.OPTIMAL:
            print("Optimal solution found with objective value:", self.eos_model.objVal)
            total_obs = sum(1 for (s, t, k), var in self.x.items() if var.x > 0.5)
            total_downlinks = sum(1 for (s, g, k), var in self.y.items() if var.x > 0.5)
            print(f"Total observations scheduled: {total_obs}")
            print(f"Total downlinks scheduled: {total_downlinks}")

            print("\n=== OBSERVATIONS ===")
            for (s, t, k), var in self.x.items():
                if var.x > 0.5:
                    print(f"  {s} observes {t} at {k}")

            print("\n=== DOWNLINKS ===")
            for (s, g, k), var in self.y.items():
                if var.x > 0.5:
                    amount = self.d[s, g, k].x if (s, g, k) in self.d else 0
                    print(f"  {s} downlinks {amount:.2f} GB to {g} at {k}")

            print("\n=== RESOURCE STATUS (Final Slot) ===")
            final_slot = self.combined_slots[-1]
            for s in self.statellite:
                mem = self.m[s, final_slot].x if (s, final_slot) in self.m else 0
                pwr = self.p[s, final_slot].x if (s, final_slot) in self.p else 0
                print(
                    f"  {s}: Memory={mem:.2f}/{self.statellite[s].memory_capacity} GB, Power={pwr:.2f}/{self.power_capacity} Wh")

        else:
            print(f"Optimization ended with status: {self.eos_model.status}")