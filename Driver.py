from GraphGenerator import GraphGenerator
from Backtracking import Backtracking
from GeneticAlgorithm import GA
from search import ArcConsistency
from SimulatedAnnealing import SimulatedAnnealing


def main():
    k_coloring = 4
    nodes = 50

    graph = GraphGenerator(nodes)
    print("SIMPLE BACKTRACKING")
    bt = Backtracking(graph, k_coloring)
    bt.backtracking()
    bt.print()

    print("=========================================================================")
    print("BACKTRACKING WITH ARC CONSISTENCY")
    ac = ArcConsistency(graph, k_coloring)
    ac.backtracking()
    ac.print()
    print("=========================================================================")
    print("GENETIC ALGORITHM")
    ga = GA(graph, k_coloring)
    ga.train()
    print("=========================================================================")
    print("SIMULATED ANNEALING")
    sa = SimulatedAnnealing(graph, k_coloring)
    sa.simulate()


main()
