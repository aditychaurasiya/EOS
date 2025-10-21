EOS: Earth Observation Scheduler

EOS is a sophisticated optimization tool designed to solve the complex challenge of scheduling Earth observation tasks for a satellite constellation. It uses mathematical optimization (Mixed-Integer Programming) with the Gurobi solver to generate an optimal observation and downlink plan that maximizes the value of collected data while respecting a wide range of operational, physical, and resource constraints.

Overview
The primary goal of this project is to determine the most effective schedule for a fleet of Earth-observing satellites. This involves deciding:

Which satellite should observe which target.
When each observation should occur.
When the collected data should be downlinked to a ground station.
The model's objective is to maximize the total "weighted value" of all observations, calculated from the urgency and importance of each target.

Project Structure
The repository is organized into distinct modules, each with a specific responsibility:

Space_OR/
├── Data/                 # Input CSV files for the model
│   ├── Satellite.csv
│   ├── Target.csv
│   ├── GroundStation.csv
│   ├── VTW.csv           # Visual Time Windows
│   └── Downlink.csv      # Downlink opportunities
├── Entities/             # Python classes for model components
├── Inputbuilder/         # Reads and parses input data
├── Solver/               # The core Gurobi optimization model
├── Outbulider/           # Generates detailed output reports
├── Output/               # Directory for all generated schedules and reports
└── main.py               # Main script to execute the scheduling process
The Optimization Model
The core of the project is a Mixed-Integer Programming (MIP) model built using the gurobipy library.

Objective Function
The model seeks to maximize the sum of the weighted values of all scheduled observations: Maximize: Σ (urgency * importance * x) where x is a binary variable indicating if an observation is scheduled.

Key Constraints
The model adheres to several critical constraints to ensure a feasible and realistic schedule:

Visual Time Window (VTW): A satellite can only observe a target if it is within a predefined VTW.
Single Observation: Each target can be observed at most once to avoid redundancy.
Observation Capacity: Each satellite has a maximum number of observations it can perform per day.
Memory Management:
Onboard memory increases with each observation.
Memory decreases when data is downlinked to a ground station.
The memory level must not exceed the satellite's storage capacity.
Downlink Windows: Data can only be downlinked during specific communication windows with a ground station.
Resource Conflicts:
A ground station can only communicate with one satellite at any given time.
A satellite can only downlink to one ground station at a time.
How to Run
Prerequisites
Python 3.x
Gurobi Solver with a valid license installed.
Required Python packages: gurobipy, pandas.
You can install the Python dependencies using pip:

pip install gurobipy pandas
Execution Steps
Clone the repository:
git clone https://github.com/aditychaurasiya/eos.git
cd eos
Customize Input Data (Optional): Modify the CSV files in the Space_OR/Data/ directory to define your own satellites, targets, and operational windows.
Run the Scheduler: Execute the main script from the root of the repository.
python Space_OR/main.py
Review the Results: The complete, optimized schedule and detailed analysis reports will be generated in the Space_OR/Output/ directory.
Input Data Format
The scheduling scenario is defined by several CSV files located in Space_OR/Data/:

Satellite.csv: Contains satellite IDs, orbit, memory capacity, and daily observation limits.
Target.csv: Lists targets with their ID, location, and assigned Urgency and Importance values.
GroundStation.csv: Defines available ground stations, their locations, and maximum data downlink rates.
VTW.csv: ("Visual Time Window") Specifies the time windows during which a specific satellite can observe a specific target.
Downlink.csv: Specifies the time windows during which a satellite can establish a communication link with a ground station for downlinking data.
Output Reports
Upon successful execution, the Outbulider module generates a comprehensive set of reports in the Space_OR/Output/ directory:

summary_report.txt: An executive summary of the optimization results, including total value captured, mission statistics, and resource utilization.
observation_schedule.csv: A detailed list of all scheduled observations, including which satellite observes which target and at what time.
target_analysis.csv: An analysis of all targets, indicating whether they were observed, their priority level, and the value captured.
satellite_utilization.csv: A report on the performance of each satellite, including the number of observations, downlinks, and overall utilization.
memory_tracking.csv: A time-step-based log of the memory usage for each satellite, showing data accumulation from observations and reduction from downlinks.
downlink_schedule.csv: A schedule of all planned data downlinks from satellites to ground stations.
eos.lp: A standard .lp file representing the mathematical model sent to Gurobi, useful for debugging and analysis
