# Class for Backtracking Algorithm
class Backtracking(object):
    def __init__(self, graph, n_coloring):
        self.domain = [i for i in range(n_coloring)]
        self.graph = graph
        self.n = n_coloring
        self.color = []
        self.num_backtracks = 0

    # Prints the Nodes
    def print(self):
        # print("Backtracking - Coloring: " + str(self.color))
        colors = []
        for i in self.graph.nodeMatrix:
            colors.append(i.color)
        print("Backtracking - Color: " + str(colors))

    # Checks if the coloring of the node is valid
    def is_safe(self, node, color, col):
        for i in range(len(self.graph.nodeMatrix)):
            if self.graph.adjMatrix[node][i] is 1 and color[i] is col:
                return False
        return True

    def backtracking(self):
        color = [0] * len(self.graph.nodeMatrix)
        if self.recursive_backtracking(self.n, color, 0) is None:
            print("--------------------------------------------------")
            print("No Solution")
            # print("Number of Backtracks: " + str(self.num_backtracks))
            return False
        print("--------------------------------------------------")
        # print(self.num_backtracks)
        return True

    def recursive_backtracking(self, k, color, node):
        if node == len(self.graph.nodeMatrix):
            return True
        for col in range(1, k+1):
            if self.is_safe(node, color, col):
                color[node] = col
                self.graph.nodeMatrix[node].color = col
                # print(color)
                if self.recursive_backtracking(k, color, node + 1):
                    return True
                color[node] = 0
                # print("BACKTRACKS! " + str(color))
                self.num_backtracks += 1

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
