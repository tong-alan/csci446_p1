from GraphGenerator import GraphGenerator
from Backtracking import Backtracking
from GeneticAlgorithm import GA
from search import ArcConsistency
from SimulatedAnnealing import SimulatedAnnealing


def main():
    k_coloring = 4
    nodes = 5
    #
    graph = GraphGenerator(nodes)
    #
    # bt = Backtracking(graph, k_coloring)
    # bt.backtracking()
    # bt.print()
    #
    # ac = ArcConsistency(graph, k_coloring)
    # ac.backtracking()
    # ac.print()
    #
    # ga = GA(graph, k_coloring)
    # ga.train()
    sa = SimulatedAnnealing(graph, k_coloring)
    sa.simulate()


main()
