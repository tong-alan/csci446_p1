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

        # Min Conflict Heuristic
        min_conflict = []
        for i in range(1,self.k+1):
            self.graph.nodeMatrix[index].color = i
            min_conflict.append(self.calc_fitness())
        min_index = sorted(range(len(min_conflict)), key=lambda k: min_conflict[k])
        for min_i in min_index:
            if coloring[index] is not min_i:
                color = min_i
                break

        coloring[index] = color
        return coloring

    def calc_fitness(self):
        num_conflicts = 0
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

    def get_current_fitness(self):
        return self.calc_single_fitness(self.current)

    def simulate(self):
        original_coloring = self.random_start()
        original_fitness = self.calc_single_fitness(original_coloring)
        temp = 10000
        while temp >= 0:
            original_coloring = self.get_current_coloring()
            original_fitness = self.get_current_fitness()
            neighbor_coloring = self.find_neighbor()
            neighbor_fitness = self.calc_single_fitness(neighbor_coloring)
            change = neighbor_fitness - self.get_current_fitness()
            if change <= 0:
                self.current = neighbor_coloring
            else:
                pass
            temp -= 1

        print(original_coloring, original_fitness)


