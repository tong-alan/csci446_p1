import random as rand

# class implementing backtracking search that maintains arc consistency
class ArcConsistency(object):
    def __init__(self, graph, n_coloring):
        self.domain = [i for i in range(n_coloring)]
        self.graph = graph
        self.n = n_coloring
        self.color = []
        self.loop_var = 0
        self.num_backtracks = 0


    # Prints the Nodes
    def print(self):
        colors = []
        for i in self.graph.nodeMatrix:
            colors.append(i.color)
        print("Arc Consistency - Color: " + str(colors))

    # makes sure each adjacent node has a possible value
    def is_consistent(self, node, color, col):
        if not self.is_safe(node, color, col):
            return False
        for i in range(len(self.graph.nodeMatrix)):
            if self.graph.adjMatrix[node][i] is 1:
                color[node] = col
                consistent = False
                for c in range(1, self.n + 1):
                    if self.is_safe(i, color, c):
                        consistent = True
                        break
                color[node] = 0

                if not consistent:
                    return False
        return True

    # Checks if the coloring of the node is valid
    def is_safe(self, node, color, col):
        for i in range(len(self.graph.nodeMatrix)):
            if self.graph.adjMatrix[node][i] is 1 and color[i] is col:
                return False
        return True

    # initiates backtracking search
    def backtracking(self):
        color = [0] * len(self.graph.nodeMatrix)
        if self.recursive_backtracking(self.n, color, 0) is None:
            print("--------------------------------------------------")
            print("No Solution")
            # print("Number of Backtracks: " + str(self.num_backtracks))
            return False

        # print(self.loop_var)
        print("--------------------------------------------------")
        # print("Number of Backtracks: " + str(self.num_backtracks))

        return True

    # variant on dfs to find coloring
    def recursive_backtracking(self, k, color, node):
        if node == len(self.graph.nodeMatrix):
            return True
        for col in range(1, k + 1):
            if self.is_consistent(node, color, col):
                color[node] = col
                self.graph.nodeMatrix[node].color = col
                # print(color)
                self.color.append(col)
                if self.recursive_backtracking(k, color, node + 1):
                    return True
                color[node] = 0
                # print("BACKTRACKS! " + str(color))
                self.num_backtracks += 1

# class implementing backtracking with forward checking
class ForwardChecking(object):
    def __init__(self, graph, n_coloring):
        self.domain = [[] for i in range(graph.size)]
        for j in range(graph.size):
            for k in range(1, n_coloring + 1):
                self.domain[j].append(k)
        self.graph = graph
        self.n = n_coloring
        self.color = []

    # Prints the Nodes
    def print(self):
        print("Forward Checking - Coloring: " + str(self.color))

    # removes color of safe node from adjacent domains
    def forward_checking(self, node, color, col):
        for i in range(len(self.graph.nodeMatrix)):
            if self.graph.adjMatrix[node][i] is 1:
                if color[i] is col:
                    return False
        if self.domain[node].count(col) > 0:
            self.domain[node].remove(col)
        return True

    # initiates backtracking search
    def backtracking(self):
        color = [0] * len(self.graph.nodeMatrix)
        if self.recursive_backtracking(self.n, color, 0) is None:
            print("No Solution")
            return False
        return True

    # variant on dfs to find coloring
    def recursive_backtracking(self, k, color, node):
        if node == len(self.graph.nodeMatrix):
            return True
        if len(self.domain[node]) != 0:
            for col in self.domain[node]:
                if self.forward_checking(node, color, col):
                    color[node] = col
                    self.graph.nodeMatrix[node].color = col
                    self.color.append(col)
                    if self.recursive_backtracking(k, color, node + 1):
                        return True
                    color[node] = 0

