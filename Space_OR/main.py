from Inputbuilder.inputbuilder import Inputbuilder
from Solver.solver import Solver
from Outbulider.outbuilder import OutputBuilder
import time

def run():
    print("Start Earth Observation Plan")
    start_time = time.time()
    input_builder = Inputbuilder()
    input_builder.build()

    solver = Solver(input_builder)
    solver.run()
    output_builder = OutputBuilder(solver, input_builder)
    output_builder.generate_all_outputs()

    print("Plan is Ready")
    print("Time taken:", round(time.time() - start_time), " seconds.")

if __name__ == '__main__':
    run()