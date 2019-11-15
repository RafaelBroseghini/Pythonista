class Graph(object):
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, key):
        return self.vertList[key]

    def addEdge(self, a, b, cost=0):
        if a not in self.vertList:
            self.addVertex(a)
        if b not in self.vertList:
            self.addVertex(b)

        self.vertList[a].addNeighbor(b, cost)

    def __getitem__(self, key):
        return self.vertList[key]

    def __str__(self):
        return str(
            {key: value.getConnections() for (key, value) in self.vertList.items()}
        )
