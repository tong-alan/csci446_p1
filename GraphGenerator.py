import secrets

class GraphGenerator(object):
    faces = 0

    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
        self.populate()

    def addEdge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        if self.checkPlanar(v1) == True:
            self.adjMatrix[v1][v2] = 1
            self.adjMatrix[v2][v1] = 1
            self.toString()
            return True
        else:
            return False

    def removeEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    #randomly populates graph with edges
    def populate(self):
        more = True
        while more != False:
            more = self.addEdge(secrets.randbelow(self.size), secrets.randbelow(self.size))


    #check planarity w/ Euler's Theorem
    def checkPlanar(self, start):
        marked = [0] * self.size
        self.countFaces(start, marked)
        edges = self.countEdges()
        print(self.faces, edges, self.size)

        #Euler's
        if ((self.faces)-(edges)+(self.size)) == 2:
            return True
        else:
            return False

    #count cycles w/ dfs
    def countFaces(self,start, marked):  
        print(start)
        if marked[start]==2:
            return

        #vertex has been visited, so there must be a cycle
        if marked == 1:
            self.faces += 1
            return

        marked[start] = 1

        #add adjacent edges to stack
        for i in range(0,self.size):
            if self.adjMatrix[start][i] == 1:
                countFaces(i, marked, stack)

        marked[start] = 2
    
    #returns number of edges
    def countEdges(self):
        edges = 0
        for i in range(0, self.size):
            self.adjMatrix[i].count(1)
        return edges

    #returns number of vertices
    def __len__(self):
        return self.size

        
    def toString(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val)),
            print
