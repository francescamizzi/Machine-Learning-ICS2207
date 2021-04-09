# importing the required libraries
import tsplib95
import time
from satsp import solver


problem = tsplib95.load('problems/pr124.tsp.txt') # loading in the data

start_time = time.time()  # starting timer to see how long algorithm takes

cities = []
templist = problem.node_coords  # getting the coordinates for all the cities

for x in range(0, len(templist)):
    city = [x+1, templist[x+1][0], templist[x+1][1]]
    cities.append(city)  # individually adding each parsed city to a new list


solver.Solve(cities, stopping_count=300)  # running the algorithm
print("Time taken: %s seconds"%(time.time() - start_time))
solver.PrintSolution()
