from GraphGenerator import GraphGenerator
from Backtracking import Backtracking


def main():
    graph10 = GraphGenerator(5)
    graph10.printMatrix()
    print(" -------------------------------- ")
    bt = Backtracking(graph10, 3)
    bt.print()
    bt.color()







main()