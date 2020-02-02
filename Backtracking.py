class Backtracking(object):
    def __init__(self, graph, n_coloring):
        self.domain = [i for i in range(n_coloring)]
        self.graph = graph
        self.n = n_coloring

    def print(self):
        for node in self.graph.nodeMatrix:
            print(node)

    def is_safe(self, node, color, col):
        for i in range(len(self.graph.nodeMatrix)):
            if self.graph.adjMatrix[node][i] == 1 and color[i] == col:
                return False
        return True

    def backtracking(self):
        color = [0] * len(self.graph.nodeMatrix)
        if self.recursive_backtracking(self.n, color, 0) is None:
            print("No Solution")
            return False
        return True

    def recursive_backtracking(self, k, color, node):
        if node == len(self.graph.nodeMatrix):
            return True

        for col in range(1, k + 1):
            if self.isSafe(node, color, col):
                color[node] = col
                self.graph.nodeMatrix[node].color = col
                if self.recursive_backtracking(k, color, node + 1):
                    return True
                color[node] = 0

    # # Experiment with using a stack instead of recursion
    # def backtracking(self):
    #     stack = [self.graph.nodeMatrix[0]]
    #     color = [1, 2, 3, 4]
    #     while len(stack) != 0:
    #         current_node = stack[-1]
    #         for i in color:
    #             if self.isSafe(current_node, i):
    #                 current_node.color = i
    #                 if any(edge.color is None for edge in current_node.edges):
    #                     for edge_node in current_node.edges:
    #                         if edge_node.color is None:
    #                             next_node = edge_node
    #                             stack.append(next_node)
    #                             break
    #                 else:
    #                     stack.pop()

















