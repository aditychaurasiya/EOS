import gurobipy as gp
from gurobipy import GRB


class Solver:
    def __init__(self, input_data):
        self.x = {}
        self.y = {}
        self.m = {}
        self.vt_window = {}
        self.downlink_window = {}

        # store input data
        self.downlink = input_data.downlink
        self.groundstation = input_data.groudstation
        self.statellite = input_data.statellite
        self.target = input_data.target
        self.vtw = input_data.vtw
        self.input_data = input_data

        self.zero = 0
        self.bigM = float('inf')
        self.data_per_obs = 5
        self.data_down = 10
        self.max_per_day_obs = 5


        self.time_slots, self.dl_time_slots = input_data._create_time_slot_mapping()

        self.env = gp.Env()
        self.eos_model = gp.Model("Earth_Observation_Scheduling", env=self.env)
        # Create combined time slots set
        self.combined_slots = sorted(set(self.time_slots + self.dl_time_slots))

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
                    self.x[s, t, k] = self.eos_model.addVar(vtype=GRB.BINARY,
                                                            name=f"x_{s}_{t}_{k.replace(':', '').replace('-', '_')}")
        # Decision variables for downlinks
        for s in self.statellite:
            for g in self.groundstation:
                for k in self.dl_time_slots:
                    self.y[s, g, k] = self.eos_model.addVar(vtype=GRB.BINARY,
                                                            name=f"y_{s}_{g}_{k.replace(':', '').replace('-', '_')}")



        # Memory variables for all combined slots
        for s in self.statellite:
            for k in self.combined_slots:
                self.m[s, k] = self.eos_model.addVar(vtype=GRB.CONTINUOUS, lb=0,
                                                     name=f"m_{s}_{k.replace(':', '').replace('-', '_')}")
        # VTW Binary Variable
        for s in self.statellite:
            for t in self.target:
                for k in self.time_slots:
                    self.vt_window[s, t, k] = self.eos_model.addVar(vtype=GRB.BINARY,
                                                            name=f"y_{s}_{t}_{k.replace(':', '').replace('-', '_')}")

        # Downlink Variable
        for s in self.statellite:
            for g in self.groundstation:
                for k in self.dl_time_slots:
                    self.downlink_window[s, g, k] = self.eos_model.addVar(vtype=GRB.BINARY,name = f"downlink_window_{s}_{g}_{k}")

    def create_constraints(self):
        # 1. VTW constraint
        self.eos_model.addConstrs(
            (self.x[s, t, k] <= self.vt_window[s, t, k]
             for s in self.statellite for t in self.target for k in self.time_slots
             if (s, t, k) in self.x),
            name="vtw_constraint"
        )

        # 2. Observation limit per day
        for s in self.statellite:
            self.eos_model.addConstr(
                gp.quicksum(self.x[s, t, k]
                            for t in self.target for k in self.time_slots
                            if (s, t, k) in self.x) <= self.max_per_day_obs,
                name=f"max_obs_per_day_{s}"
            )

        # 3. Single observation per target
        for t in self.target:
            obs_sum = gp.quicksum(self.x[s, t, k]
                                  for s in self.statellite
                                  for k in self.time_slots
                                  if (s, t, k) in self.x)
            # obs_sum is a LinExpr; size() works but is optional — keep constraint only if expr non-empty
            try:
                if obs_sum.size() > 0:
                    self.eos_model.addConstr(obs_sum <= 1, name=f"single_obs_{t}")
            except AttributeError:
                # some gurobi versions/contexts may not implement size() on LinExpr; still safe to add
                self.eos_model.addConstr(obs_sum <= 1, name=f"single_obs_{t}")

        # 4/5. Memory balance & Memory capacity over combined slots
        for s in self.statellite:
            for idx, k in enumerate(self.combined_slots):
                if idx == 0:
                    # use k (first combined slot) as initial slot key, not literal 0
                    self.eos_model.addConstr(self.m[s, k] == self.zero, name=f"mem_initial_{s}")
                else:
                    prev_k = self.combined_slots[idx - 1]

                    obs_in = gp.quicksum(
                        self.data_per_obs * self.x[s, t, prev_k]
                        for t in self.target
                        if (s, t, prev_k) in self.x
                    )

                    dl_out = gp.quicksum(
                        self.data_down * self.y[s, g, prev_k]
                        for g in self.groundstation
                        if (s, g, prev_k) in self.y
                    )

                    self.eos_model.addConstr(
                        self.m[s, k] == self.m[s, prev_k] + obs_in - dl_out,
                        name=f"memory_balance_{s}_{k.replace(':', '').replace('-', '_')}"
                    )

        # 5b. Memory Capacity Constraint for downlink slots
        for s in self.statellite:
            for k in self.dl_time_slots:
                self.eos_model.addConstr(
                    self.m[s, k] <= self.statellite[s].memory_capacity,
                    name=f"memory_capacity_{s}_{k.replace(':', '').replace('-', '_')}"
                )

        # 6. Downlink window (enforce y <= downlink_window variable)
        for s in self.statellite:
            for g in self.groundstation:
                for k in self.dl_time_slots:
                    self.eos_model.addConstr(
                        self.y[s, g, k] <= self.downlink_window[s, g, k],
                        name=f"downlink_window_{s}_{g}_{k.replace(':', '').replace('-', '_')}"
                    )
                    # Removed the `if self.downlink_window[...] == self.zero:` check because
                    # it tries to evaluate a Gurobi Var as a Python bool. If you need y==0
                    # when a parameter is 0, make downlink_window a param and check it here.

        # 7. Ground station conflict
        for g in self.groundstation:
            for k in self.dl_time_slots:
                self.eos_model.addConstr(
                    gp.quicksum(self.y[s, g, k]
                                for s in self.statellite
                                if (s, g, k) in self.y) <= 1,
                    name=f"groundstation_conflict_{g}_{k.replace(':', '').replace('-', '_')}"
                )

        # 8. Satellite downlink exclusivity
        for s in self.statellite:
            for k in self.dl_time_slots:
                self.eos_model.addConstr(
                    gp.quicksum(self.y[s, g, k]
                                for g in self.groundstation
                                if (s, g, k) in self.y) <= 1,
                    name=f"satellite_downlink_exclusivity_{s}_{k.replace(':', '').replace('-', '_')}"
                )

    def create_objective(self):
        objective = gp.quicksum(self.target[t].urgency * self.target[t].importance * self.x[s, t, k]
                                for s in self.statellite
                                for t in self.target
                                for k in self.time_slots
                                if (s, t, k) in self.x)
        self.eos_model.setObjective(objective, GRB.MAXIMIZE)

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
        else:
            print(f"Optimization ended with status: {self.eos_model.status}")
