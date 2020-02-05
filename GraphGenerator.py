import secrets

# Graph Generator Class. Creates an adjacency matrix and planar graph for our algorithms.

# Graph is represented with adjacency matrix
class GraphGenerator(object):
    def __init__(self, size):
        self.faces = 1
        self.adjMatrix = []
        # Used for testing.
        # self.adjMatrix = [
        #      [0,1,1,1],
        #     [1,0,1,1],
        #     [1,1,0,1],
        #     [1,1,1,0]
        # ]
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
        self.populate()
        # Convert the adjacency matrix to node based edges rather than just 1 to represent an edge.
        self.nodeMatrix = self.convert_to_nodes()

    # adds a new edge to the adjacency matrix
    def printAJ(self):
        print("Adjacency Matrix")
        for i in self.adjMatrix:
            print(i)
        print()

    def addEdge(self, v1, v2):
        if v1 == v2:
            return

        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removedge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    # randomly populates graph with edges
    def populate(self):
        more = True

        # guarantees connected graph
        for i in range(self.size * 2):
            rand = i
            if rand >= self.size:
                self.addEdge(secrets.randbelow(self.size), secrets.randbelow(self.size))
                continue
            while rand == i or self.adjMatrix[i][rand] == 1:
                rand = secrets.randbelow(self.size)

            self.addEdge(i, rand)

    # Creates a node based equivalent of the adjacency matrix for easier modification to the coloring assignments
    def convert_to_nodes(self):
        matrix = [Node(i) for i in range(len(self.adjMatrix))]
        for i, node in enumerate(self.adjMatrix):
            for j, edges in enumerate(node):
                if edges == 1:
                    matrix[i].add_edges(matrix[j])
        return matrix

    # Prints the graph, node-based
    def printNodes(self):
        for node in self.nodeMatrix:
            print(node)

    # Returns the node matrix.
    def get_nodeMatrix(self):
        return self.nodeMatrix

    # returns number of edges
    def countEdges(self):
        edges = 0
        for i in range(0, self.size):
            self.adjMatrix[i].count(1)
        return edges

    # returns number of vertices
    def __len__(self):
        return self.size

    def printMatrix(self):
        for row in self.adjMatrix:
            print(row)
            print

# Node class for our node matrix. A node will hold a value, which will be the name of the Node, list of Nodes that
# represents the edges, and the color of that node, originally set to none.
class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.color = None

    def add_edges(self, node):
        self.edges.append(node)

    def __str__(self):
        nodes = ""
        for edge in self.edges:
            nodes += str(edge.value) + ", "
        return "(Name) " + str(self.value) + ": (Edges) [" + nodes[:-2] + "]: (Color) " + str(self.color)
