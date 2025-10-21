import gurobipy as gp
from gurobipy import GRB


class Solver:
    def __init__(self, input_data):
        self.x = {}
        self.y = {}
        self.d = {}  # downlink amount variable
        self.m = {}
        self.vt_window = {}
        self.downlink_window = {}

        # Store input data
        self.downlink = input_data.downlink
        self.groundstation = input_data.groudstation
        self.statellite = input_data.statellite
        self.target = input_data.target
        self.vtw = input_data.vtw
        self.input_data = input_data

        # Constants and Parameters
        self.zero = 0
        self.bigM = float('inf')
        self.data_per_obs = 5
        self.data_down = 10
        self.max_per_day_obs = 5

        # Time Slots
        self.time_slots, self.dl_time_slots = input_data._create_time_slot_mapping()
        self.combined_slots = sorted(set(self.time_slots + self.dl_time_slots))

        # Parameter dictionaries from input data
        self._build_vtw_parameters()
        self._build_downlink_parameters()

        # Env
        self.env = gp.Env()
        self.eos_model = gp.Model("Earth_Observation_Scheduling", env=self.env)

    def _build_vtw_parameters(self):
        """Build VTW binary parameters from input data"""
        # Initialize all to 0
        for s in self.statellite:
            for t in self.target:
                for k in self.time_slots:
                    self.vt_window[s, t, k] = 0

        # Set to 1 where VTW exists
        vtw_count = 0
        for vtw_obj in self.vtw.values():
            s = vtw_obj.satelliteid
            t = vtw_obj.target_id
            k = vtw_obj.timeSlotStart.strip()

            if s in self.statellite and t in self.target and k in self.time_slots:
                self.vt_window[s, t, k] = 1
                vtw_count += 1

    def _build_downlink_parameters(self):
        """Build downlink window binary parameters from input data"""
        # Initialize all to 0
        for s in self.statellite:
            for g in self.groundstation:
                for k in self.dl_time_slots:
                    self.downlink_window[s, g, k] = 0

        # Set to 1 where downlink window exists
        dl_count = 0
        print("\n=== BUILDING DOWNLINK PARAMETERS ===")
        for dl_obj in self.downlink.values():
            s = dl_obj.satelliteid
            g = dl_obj.groundstationid
            k = dl_obj.timeSlotStart.strip()

          
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

        # Decision variables for downlink amount (continuous, 0 to 10 GB)
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

    def create_constraints(self):
        # 1. VTW constraint - can only observe during available windows
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
        # Memory at slot k = Memory at slot (k-1) + observations at k - downlinks at k
        print("\n=== MEMORY BALANCE CONSTRAINTS DEBUG ===")
        for s in self.statellite:
            for idx, k in enumerate(self.combined_slots):
                if idx == 0:
                    # Initial memory = observations at first slot - downlinks at first slot
                    obs_in = gp.quicksum(
                        self.data_per_obs * self.x[s, t, k]
                        for t in self.target
                        if (s, t, k) in self.x
                    )

                    # Use variable downlink amount d instead of fixed data_down * y
                    dl_out = gp.quicksum(
                        self.d[s, g, k]
                        for g in self.groundstation
                        if (s, g, k) in self.d
                    )

                    print(
                        f"{s} at {k}: Initial = obs_in - dl_out (dl terms: {len([1 for g in self.groundstation if (s, g, k) in self.d])})")

                    self.eos_model.addConstr(
                        self.m[s, k] == obs_in - dl_out,
                        name=f"mem_initial_{s}"
                    )

                else:
                    prev_k = self.combined_slots[idx - 1]

                    # Observations at CURRENT slot k
                    obs_in = gp.quicksum(
                        self.data_per_obs * self.x[s, t, k]
                        for t in self.target
                        if (s, t, k) in self.x
                    )

                    # Use variable downlink amount d instead of fixed data_down * y
                    dl_out = gp.quicksum(
                        self.d[s, g, k]
                        for g in self.groundstation
                        if (s, g, k) in self.d
                    )

                    num_dl_terms = len([1 for g in self.groundstation if (s, g, k) in self.d])
                    if num_dl_terms > 0:
                        print(f"{s} at {k}: m[{k}] = m[{prev_k}] + obs - dl (dl terms: {num_dl_terms})")

                    self.eos_model.addConstr(
                        self.m[s, k] == self.m[s, prev_k] + obs_in - dl_out,
                        name=f"memory_balance_{s}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                    )

        print()

        # 5. Memory capacity constraint
        for s in self.statellite:
            for k in self.combined_slots:
                self.eos_model.addConstr(
                    self.m[s, k] <= self.statellite[s].memory_capacity,
                    name=f"memory_capacity_{s}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                )

        # 6. Downlink window constraint - can only downlink during available windows
        for s in self.statellite:
            for g in self.groundstation:
                for k in self.dl_time_slots:
                    if (s, g, k) in self.y:
                        self.eos_model.addConstr(
                            self.y[s, g, k] <= self.downlink_window[s, g, k],
                            name=f"downlink_window_{s}_{g}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                        )

        # 6.5. Link downlink amount to binary decision
        # d can only be > 0 if y = 1 (downlink window is used)
        for s in self.statellite:
            for g in self.groundstation:
                for k in self.dl_time_slots:
                    if (s, g, k) in self.y and (s, g, k) in self.d:
                        self.eos_model.addConstr(
                            self.d[s, g, k] <= self.data_down * self.y[s, g, k],
                            name=f"link_downlink_amount_{s}_{g}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                        )

        # 7. Ground station conflict - one satellite per ground station per slot
        for g in self.groundstation:
            for k in self.dl_time_slots:
                self.eos_model.addConstr(
                    gp.quicksum(self.y[s, g, k]
                                for s in self.statellite
                                if (s, g, k) in self.y) <= 1,
                    name=f"groundstation_conflict_{g}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                )

        # 8. Satellite downlink exclusivity - one ground station per satellite per slot
        for s in self.statellite:
            for k in self.dl_time_slots:
                self.eos_model.addConstr(
                    gp.quicksum(self.y[s, g, k]
                                for g in self.groundstation
                                if (s, g, k) in self.y) <= 1,
                    name=f"satellite_downlink_exclusivity_{s}_{k.replace(':', '').replace('-', '_').replace('–', '_')}"
                )

    def create_objective(self):
        # Primary: maximize observation value
        obs_value = gp.quicksum(
            self.target[t].urgency * self.target[t].importance * self.x[s, t, k]
            for s in self.statellite
            for t in self.target
            for k in self.time_slots
            if (s, t, k) in self.x
        )

        # # Secondary: STRONGLY encourage downlinks with very high weight
        # downlink_value = 1000 * gp.quicksum(
        #     self.y[s, g, k]
        #     for s in self.statellite
        #     for g in self.groundstation
        #     for k in self.dl_time_slots
        #     if (s, g, k) in self.y
        # )

        
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
                    print(f"  {s} downlinks to {g} at {k}: {amount:.2f} GB")

            print("\n=== MEMORY STATUS (All Slots) ===")
            for s in self.statellite:
                print(f"\n{s}:")
                for k in self.combined_slots:
                    if (s, k) in self.m:
                        print(f"  {k}: {self.m[s, k].x:.2f} GB")

            print("\n=== DOWNLINK VARIABLES DEBUG ===")
            print("Checking y and d variables:")
            for s in self.statellite:
                for g in self.groundstation:
                    for k in self.dl_time_slots:
                        if (s, g, k) in self.y:
                            window_val = self.downlink_window.get((s, g, k), "NOT FOUND")
                            d_val = self.d[s, g, k].x if (s, g, k) in self.d else "N/A"
                            print(
                                f"  y[{s},{g},{k}] = {self.y[s, g, k].x:.2f}, d[{s},{g},{k}] = {d_val:.2f} GB, window = {window_val}")

        else:
            print(f"Optimization ended with status: {self.eos_model.status}")
