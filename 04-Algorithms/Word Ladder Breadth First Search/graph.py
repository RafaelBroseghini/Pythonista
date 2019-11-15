class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.pred = None
        self.distance = 0

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return [v.id for v in self.connectedTo.keys()]

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def getDistance(self):
        return self.distance

    def setDistance(self, dis):
        self.distance = dis

    def setPred(self, v):
        self.pred = v

    def getPred(self):
        return self.pred


class Graph:
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

    def __contains__(self, key):
        return key in self.vertList

    def __getitem__(self, key):
        return self.vertList[key]

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nt = self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
