

class Backtracking(object):
    def __init__(self, graph, n_coloring):
        self.graph = graph
        self.map = self.color()
        self.n = n_coloring

    def print(self):
        for node in self.graph.nodeMatrix:
            print(node)

    def color(self):
        for node in self.graph.nodeMatrix:
            pass
        map = []
        for row in range(len(self.graph.adjMatrix)):
            map.append([self.graph.adjMatrix[row], row])

    def backtracking(self):
        pass




