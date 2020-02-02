from GraphGenerator import GraphGenerator
import search

def main():
    graph10 = GraphGenerator(10)
    graph20 = GraphGenerator(20)
    graph30 = GraphGenerator(30)
    graph40 = GraphGenerator(40)
    graph50 = GraphGenerator(50)
    graph60 = GraphGenerator(60)
    graph70 = GraphGenerator(70)
    graph80 = GraphGenerator(80)
    graph90 = GraphGenerator(90)
    graph100 = GraphGenerator(100)
    
    graph10.toString()
    graph20.toString()
    graph30.toString()

    four_backtrack = Backtracking(graph10)

main()