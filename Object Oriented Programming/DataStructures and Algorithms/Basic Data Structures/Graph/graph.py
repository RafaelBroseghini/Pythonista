class Vertex():
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
        
    def getConnections(self):
        return "Connected to: {}".format([v.id for v in self.connectedTo.keys()])
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
    
class Graph():
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self,key):
        return self.vertList[key]
    
    def __contains__(self,key):
        return key in self.vertList
    
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nt = self.addVertex(t)
        
        self.vertList[f].addNeighbor(self.vertList[t],cost)
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
    

# make file with fake ip adresses and connect them using graph
def main():
    g = Graph()

    for i in range(11):
        g.addVertex(i)
        
    print(g.vertList)
    print()

    g.addEdge(1,2,5)

    for v in g:
        print(v.id, v.getConnections())
        print()
if __name__ == '__main__':
    main()
