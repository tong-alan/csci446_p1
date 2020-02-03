import random
from copy import copy

class SimulatedAnnealing(object):
    def __init__(self, graph, k_coloring):
        self.graph = graph
        self.k = k_coloring
        self.temperature = None
        self.current = None

    def random_start(self):
        coloring = [random.randint(1, self.k) for i in range(len(self.graph.nodeMatrix))]
        for i, node in enumerate(self.graph.nodeMatrix):
            self.graph.nodeMatrix[i].color = coloring[i]
        self.current = coloring
        return coloring

    def find_neighbor(self):
        coloring = copy(self.current)
        index = random.randint(0, len(self.graph.nodeMatrix) - 1)
        color = random.randint(1, self.k)
        coloring[index] = color
        return coloring

    def calc_fitness(self):
        num_conflicts = self.k
        for node in self.graph.nodeMatrix:
            for edge in node.edges:
                if node.color == edge.color:
                    num_conflicts += 1
        return num_conflicts

    def calc_single_fitness(self, vector):
        for i, node in enumerate(self.graph.nodeMatrix):
            self.graph.nodeMatrix[i].color = vector[i]
        return self.calc_fitness()

    def get_current_coloring(self):
        return self.current


    def simulate(self):
        original_coloring = self.random_start()
        original_fitness = self.calc_single_fitness(original_coloring)

        neighbor_coloring = self.find_neighbor()
        neighbor_fitness = self.calc_single_fitness(neighbor_coloring)
        if original_fitness >= neighbor_fitness:
            self.current = original_coloring











