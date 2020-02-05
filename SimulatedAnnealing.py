import random
from copy import copy
import math

TEMPERATURE = 10000


# Class for simulated annealing algorithm
class SimulatedAnnealing(object):
    def __init__(self, graph, k_coloring):
        self.graph = graph
        self.k = k_coloring
        self.temperature = None
        self.current = None

    # Randomly select a coloring, regardless of the validity
    def random_start(self):
        coloring = [random.randint(1, self.k) for i in range(len(self.graph.nodeMatrix))]
        for i, node in enumerate(self.graph.nodeMatrix):
            self.graph.nodeMatrix[i].color = coloring[i]
        self.current = coloring
        return coloring

    # Randomly change one color of the coloring from our current state, represented as the "neighbor"
    def find_neighbor(self):
        coloring = copy(self.current)
        index = random.randint(0, len(self.graph.nodeMatrix) - 1)

        # # Min Conflict Heuristic
        # min_conflict = []
        # for i in range(1, self.k+1):
        #     self.graph.nodeMatrix[index].color = i
        #     min_conflict.append(self.calc_fitness())
        # min_index = sorted(range(len(min_conflict)), key=lambda k: min_conflict[k])
        # for min_i in min_index:
        #     if coloring[index] is not min_i:
        #         color = min_i+1
        #         break

        # Random Neighbor
        color = random.randint(1, self.k)

        coloring[index] = color
        return coloring

    # Calculate the number of conflicted edges.
    def calc_fitness(self):
        num_conflicts = 0
        for node in self.graph.nodeMatrix:
            for edge in node.edges:
                if node.color == edge.color:
                    num_conflicts += 1
        return num_conflicts

    # Calculates the number of conflicted edges for a given vector.
    def calc_single_fitness(self, vector):
        for i, node in enumerate(self.graph.nodeMatrix):
            self.graph.nodeMatrix[i].color = vector[i]
        return self.calc_fitness()

    # Returns the current coloring of the algorithm
    def get_current_coloring(self):
        return self.current

    # Returns the current coloring fitness of the algorithm.
    def get_current_fitness(self):
        return self.calc_single_fitness(self.current)

    # Simulates the algorithm. Starting with a temperature of 10000
    def simulate(self):
        original_coloring = self.random_start()
        original_fitness = self.calc_single_fitness(original_coloring)
        temp = TEMPERATURE
        while temp >= 0:
            # print("SA - Coloring: " + str(self.get_current_coloring()) + " Conflicts: " + str(
            #      self.get_current_fitness() / 2))
            original_coloring = self.get_current_coloring()
            original_fitness = self.get_current_fitness()
            neighbor_coloring = self.find_neighbor()
            neighbor_fitness = self.calc_single_fitness(neighbor_coloring)
            change = neighbor_fitness - original_fitness
            # Simulated annealing in action
            if change <= 0: # Always accept better state.
                self.current = neighbor_coloring
            else:
                # Accept worst state based on our probability.
                bolzmann = math.exp(- temp * change)
                if flip(bolzmann):
                    self.current = neighbor_coloring
                else:
                    self.current = original_coloring
            # Schedule of our simulated annealing algorithm.
            temp -= 1
        print("Global \"Minimum\"")
        print("Temperature: " + str(temp+1))
        print("SA - Coloring: " + str(original_coloring) + " Conflicts: " + str(original_fitness/2))


# Coin simulation based on a probability.
def flip(prob):
    return True if random.random() < prob else False
