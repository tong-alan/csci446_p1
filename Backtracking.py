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

    # Initiates backtracking search
    def backtracking(self):
        color = [0] * len(self.graph.nodeMatrix)
        if self.recursive_backtracking(self.n, color, 0) is None:
            print("No Solution")
            # print("Number of Backtracks: " + str(self.num_backtracks))
            return False
        # print(self.num_backtracks)
        return True

    # Recursively checks to move forward with the backtracking. Variant on dfs to find coloring using recursion.
    def recursive_backtracking(self, k, color, node):
        if node == len(self.graph.nodeMatrix):
            return True
        for col in range(1, k+1):
            if self.is_safe(node, color, col):
                # If the coloring is safe, we will assign that color to the node.
                color[node] = col
                self.graph.nodeMatrix[node].color = col
                # print(color)
                if self.recursive_backtracking(k, color, node + 1):
                    return True
                color[node] = 0
                # Here we will backtrack to our previous recursive function to adjust our previous colorings.
                # print("BACKTRACKS! " + str(color))
                self.num_backtracks += 1

