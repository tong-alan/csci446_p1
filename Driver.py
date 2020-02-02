from GraphGenerator import GraphGenerator
from Backtracking import Backtracking


def main():
    graph10 = GraphGenerator(10)
    graph10.printMatrix()
    print(" -------------------------------- ")
    bt = Backtracking(graph10, 3)
    bt.print()







main()