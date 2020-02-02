from GraphGenerator import GraphGenerator
from Backtracking import Backtracking


def main():
    graph10 = GraphGenerator(10)
    bt = Backtracking(graph10, 4)
    bt.backtracking()
    bt.print()

main()