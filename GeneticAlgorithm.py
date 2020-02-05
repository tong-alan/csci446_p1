import random

# Tunable Parameters, we found this to yield the best results
POPULATION_SIZE = 100
CONVERGENCE_SIZE = 5000
CONVERGENCE_THRESHOLD = 0.01


# Genetic Algorithm for Graph Coloring
class GA(object):
    def __init__(self, graph, k):
        self.graph = graph
        self.k = k
        self.population = self.create_initial_population()
        self.evaluate_fitness()
        self.most_fit = None

    # Randomly creates individual from the population
    def create_initial_population(self):
        population = []
        for i in range(POPULATION_SIZE):
            coloring = [random.randint(1, self.k) for i in range(len(self.graph.nodeMatrix))]
            population.append(Individual(coloring))
        return population

    # Assigns a fitness score to all members of the population
    def evaluate_fitness(self):
        num_nodes = len(self.graph.nodeMatrix)
        for individual in self.population:
            for i in range(num_nodes):
                self.graph.nodeMatrix[i].color = individual.coloring[i]
                individual.fitness = self.calc_fitness()

    # Fitness function that returns the number of conflicts in the graph based on the coloring currently in the graph
    def calc_fitness(self):
        num_conflicts = 0
        for node in self.graph.nodeMatrix:
            for edge in node.edges:
                if node.color == edge.color:
                    num_conflicts += 1
        return num_conflicts

    # Calculates a single fitness for a given vector/coloring
    def calc_single_fitness(self, vector):
        for i, node in enumerate(self.graph.nodeMatrix):
            self.graph.nodeMatrix[i].color = vector[i]
        return self.calc_fitness()

    # Selects our mating pool
    def parent_selection(self):
        # Tournament Selection
        selected_individuals = []
        for i in range(POPULATION_SIZE):
            parent_one = self.population[random.randint(0, POPULATION_SIZE-1)]
            parent_two = self.population[random.randint(0, POPULATION_SIZE-1)]
            # Minimizing the fitness
            if parent_one.fitness < parent_two.fitness:
                selected_individuals.append(parent_one)
            else:
                selected_individuals.append(parent_two)
        return selected_individuals

    def recombine(self, new_population):
        # Generational Replacement
        self.population = new_population

    # Binomial Crossover, input two parents will result in an output of two offspring
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

    # Create offspring population based on parent population
    def offspring(self, parents):
        offspring = []
        for i in range(0,len(self.population),2):
            offspring_one, offspring_two = self.crossover(parents[i], parents[i+1])
            offspring.append(offspring_one)
            offspring.append(offspring_two)
        return offspring

    # Simulates the genetic algorithm
    def train(self):
        fitness_history = []
        global_best_individual = self.population[0]
        generation = 0
        while True:
            parents = self.parent_selection()
            offspring = self.offspring(parents)
            self.recombine(offspring)
            generation += 1
            # We keep track of the global best individual we have seen so far.
            for individual in self.population:
                if global_best_individual.fitness > individual.fitness:
                    global_best_individual = individual
                fitness_history.append(individual.fitness)
            # Convergence testing. If the fitness improves by only our CONVERGENCE_THRESHOLD, then we terminate the
            # algorithm.
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


# Individual class to aid our genetic algorithm process.
class Individual(object):
    def __init__(self, coloring):
        self.coloring = coloring
        self.fitness = None

    def __str__(self):
        return "Coloring: " + str(self.coloring) + " Fitness: " + str(self.fitness/2)


