from GraphGenerator import GraphGenerator
from Backtracking import Backtracking
from GeneticAlgorithm import GA


def main():

    k_coloring = 4
    nodes = 5

    graph = GraphGenerator(nodes)

    bt = Backtracking(graph, k_coloring)
    bt.backtracking()
    bt.print()

    ga = GA(graph, k_coloring)
    ga.train()



main()