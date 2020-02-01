

class Backtracking(object):
    def __init__(self, graph):
        self.graph = graph
        self.map = self.color()

    def color(self):
        map = ()
        for row in range(len(self.graph.adjMatrix)):
            print(self.graph.adjMatrix[row])

