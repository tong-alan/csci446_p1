class GA(object):
    def __init__(self, graph, k, mutation_rate, crossover_probability, tournamet_size, convergence_size):
        self.graph = graph
        self.k = k

    def convert_to_vector(self):
        pass

    def convert_to_matrix(self):
        pass

    def parent_selection(self):
        pass

    def offspring(self):
        pass

    def replacement(self):
        pass

    def crossover(self, parent_one, parent_two):
        pass

    def train(self):
        pass

class Individual(object):
    def __init__(self, vector):
        self.vector = vector

    def calc_fitness(self):
        pass


