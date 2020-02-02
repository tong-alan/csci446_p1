

class Backtracking(object):
    def __init__(self, graph, n_coloring):
        self.domain = [i for i in range(n_coloring)]
        self.graph = graph
        self.n = n_coloring

    def print(self):
        for node in self.graph.nodeMatrix:
            print(node)

    def isSafe(self, node, color):
        for connected_nodes in self.graph.nodeMatrix:
            if connected_nodes.color is color:
                return False
        return True


    def color(self):
        colors = [None for i in range(len(self.graph.nodeMatrix))]


    def backtracking(self):





