from GraphGenerator import GraphGenerator
from Backtracking import Backtracking
from GeneticAlgorithm import GA
from search import ForwardChecking
from search import ArcConsistency
from SimulatedAnnealing import SimulatedAnnealing


def main():
    k_coloring = 4
    nodes = 20
    #
    graph = GraphGenerator(nodes)
    #
    bt = Backtracking(graph, k_coloring)
    bt.backtracking()
    bt.print()

    ac = ArcConsistency(graph, k_coloring)
    ac.backtracking()
    ac.print()

    fc = ForwardChecking(graph, k_coloring)
    fc.backtracking()
    fc.print()

    ga = GA(graph, k_coloring)
    ga.train()
    sa = SimulatedAnnealing(graph, k_coloring)
    sa.simulate()


main()
