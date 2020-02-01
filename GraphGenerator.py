import secrets

class GraphGenerator(object):
    def __init__(self, size):
        self.faces = 1
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
        self.populate()

    def addEdge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
            return
        
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        self.toString()
        

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

        #guarantees connected graph
        for i in range(self.size):
            rand = i
            while rand == i and self.adjMatrix[i][rand] != 1:
                rand = secrets.randbelow(self.size)

            self.addEdge(i,rand)
        self.toString()
        print(" ")


   #     while more == True:
   #         start = secrets.randbelow(self.size)
   #         self.addEdge(start, secrets.randbelow(self.size))
   #         more = self.checkPlanar(start)
        return


    #check planarity w/ Euler's Theorem
    #def checkPlanar(self, start):
    #    if self.countEdges == 0:
    #        return True
    #    marked = [0] * self.size
    #    parent = [[]] * self.size
    #    self.countFaces(-1, start, marked, parent)
    #    edges = self.countEdges()
    #    print(self.countFaces, self.countEdges, self.size)

    #    #Euler's
    #    if ((self.faces)-(edges)+(self.size)) == 2:
    #        return True
    #    else:
    #        return False

    ##count cycles w/ dfs
    #def countFaces(self,prev, start, marked, parent):  
    #    print(start)
    #    print(marked[start])
    #    print(self.faces)
    #    print(parent[start])
    #    if marked[start]==2:
    #        return self.faces

    #    #vertex has been visited, so there must be a cycle
    #    if marked == 1:
    #        print("working!")
    #        self.faces += 1
    #        return self.faces
    #    parent[start].append(prev)
    #    print(prev)

    #    marked[start] = 1

    #    #add adjacent edges to stack
    #    for i in range(0,self.size):
    #        if self.adjMatrix[start][i] == 1 and prev != i and marked[i] != 2:
    #            if parent[start].count(i) < 2:
    #                self.faces = self.countFaces(start, i, marked, parent)
    #        else:
    #            continue

    #    marked[start] = 2
    #    return self.faces
    
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
            print(row)
            print
