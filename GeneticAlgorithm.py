import random

POPULATION_SIZE = 100
CONVERGENCE_SIZE = 5000
CONVERGENCE_THRESHOLD = 0.01


class GA(object):
    def __init__(self, graph, k):
        self.graph = graph
        self.k = k
        self.population = self.create_initial_population()
        self.evaluate_fitness()
        self.most_fit = None

    def create_initial_population(self):
        population = []
        for i in range(POPULATION_SIZE):
            coloring = [random.randint(1, self.k) for i in range(len(self.graph.nodeMatrix))]
            population.append(Individual(coloring))
        return population

    def evaluate_fitness(self):
        num_nodes = len(self.graph.nodeMatrix)
        for individual in self.population:
            for i in range(num_nodes):
                self.graph.nodeMatrix[i].color = individual.coloring[i]
                individual.fitness = self.calc_fitness()

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

    def parent_selection(self):
        # Tournament Selection
        selected_individuals = []
        for i in range(POPULATION_SIZE):
            parent_one = self.population[random.randint(0, POPULATION_SIZE-1)]
            parent_two = self.population[random.randint(0, POPULATION_SIZE-1)]
            if parent_one.fitness < parent_two.fitness:
                selected_individuals.append(parent_one)
            else:
                selected_individuals.append(parent_two)
        return selected_individuals

    def recombine(self, new_population):
        self.population = new_population

    def crossover(self, parent_one, parent_two):
        child_a = []
        child_b = []
        for i in range(len(parent_one.coloring)):
            if flip(0.5):
                child_a.append(parent_two.coloring[i])
                child_b.append(parent_one.coloring[i])
            else:
                child_a.append(parent_one.coloring[i])
                child_b.append(parent_two.coloring[i])
        fitness_one = self.calc_single_fitness(child_a)
        fitness_two = self.calc_single_fitness(child_b)
        child_one = Individual(child_a)
        child_two = Individual(child_b)
        child_one.fitness = fitness_one
        child_two.fitness = fitness_two
        return child_one, child_two

    def offspring(self, parents):
        offspring = []
        for i in range(0,len(self.population),2):
            offspring_one, offspring_two = self.crossover(parents[i], parents[i+1])
            offspring.append(offspring_one)
            offspring.append(offspring_two)
        return offspring

    def train(self):
        fitness_history = []
        global_best_individual = self.population[0]
        while True:
            parents = self.parent_selection()
            offspring = self.offspring(parents)
            self.recombine(offspring)
            for individual in self.population:
                if global_best_individual.fitness > individual.fitness:
                    global_best_individual = individual
                fitness_history.append(individual.fitness)

            if len(fitness_history) > CONVERGENCE_SIZE * 2:
                fitness_history.pop(0)
                older_fitness = sum(fitness_history[:CONVERGENCE_SIZE])
                newer_fitness = sum(fitness_history[CONVERGENCE_SIZE:])
                if newer_fitness <= older_fitness + CONVERGENCE_THRESHOLD:
                    print("GA - " + str(global_best_individual))
                    return


# Coin simulation based on a probability.
def flip(prob):
    return True if random.random() < prob else False


class Individual(object):
    def __init__(self, coloring):
        self.coloring = coloring
        self.fitness = None

    def __str__(self):
        return "Coloring: " + str(self.coloring) + " Fitness: " + str(self.fitness)


