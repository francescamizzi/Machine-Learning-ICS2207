import tsplib95
import acopy

# setting up the environment
solver = acopy.Solver(rho=.03, q=1)
colony = acopy.Colony(alpha=1, beta=3)

# adding a timer to record the total time to find the best path
timer = acopy.plugins.Timer()
solver.add_plugin(timer)

# setting it up so that is prints out each iteration
printout = acopy.plugins.Printout()
solver.add_plugin(printout)

problem = tsplib95.load('problems/pr124.tsp.txt')  # loading in the dataset
G = problem.get_graph()  # changing the dataset so that it can be used by the algorithm

tour = solver.solve(G, colony, limit=100)  #running the algorithm

# printing out relevant information
print("Shortest tour: ", tour.cost)
print("Best tour: ", tour.nodes)
print("Time to complete: ", timer.duration)

