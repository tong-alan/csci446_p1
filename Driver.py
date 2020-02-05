from GraphGenerator import GraphGenerator
from Backtracking import Backtracking
from GeneticAlgorithm import GA
from search import ForwardChecking
from search import ArcConsistency
from SimulatedAnnealing import SimulatedAnnealing

# Entry point for our program. Here we execute all 5 of our algorithms.

def main():
    # Tuning based on user
    k_coloring = 4
    nodes = 10

    # Graph Generator
    graph = GraphGenerator(nodes)
    graph.printAJ()

    # Algorithms
    # Simple Backtracking
    print("SIMPLE BACKTRACKING")
    bt = Backtracking(graph, k_coloring)
    bt.backtracking()
    bt.print()

    # Backtracking with arc consistency
    print("=========================================================================")
    print("BACKTRACKING WITH ARC CONSISTENCY")
    ac = ArcConsistency(graph, k_coloring)
    ac.backtracking()
    ac.print()

    # Backtracking with forward checking
    print("=========================================================================")
    print("BACKTRACKING WITH FORWARD CHECKING")
    fc = ForwardChecking(graph, k_coloring)
    fc.backtracking()
    fc.print()

    # Local Search Genetic Algorithm
    print("=========================================================================")
    print("GENETIC ALGORITHM")
    ga = GA(graph, k_coloring)
    ga.train()

    # Local Search Simulated Annealing
    print("=========================================================================")
    print("SIMULATED ANNEALING")
    sa = SimulatedAnnealing(graph, k_coloring)
    sa.simulate()


main()
