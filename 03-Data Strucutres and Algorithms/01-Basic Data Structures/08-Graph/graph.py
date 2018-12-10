class Vertex():
    def __init__(self, key):
        self.id = key
        # Dictionary with neighbors as keys and distances to them as values.
        self.connectedTo = {}
        
    #Add neighbor with specified weight (distance) parameter.
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    
    # Get all neighbors keys. Str type. Method can be changed to return list with nbrs.
    def getConnections(self):
        return "Connected to: {}".format([v.id for v in self.connectedTo.keys()])
    
    # Return Vertex id.
    def getId(self):
        return self.id
    
    # Return distance to neighbor passed as parameter.
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
    
class Graph():
    def __init__(self):
        # Dictionary with all vertices in graph as keys and their dict(neighbors: distance) as valuee.
        self.vertList = {}
        self.numVertices = 0
    
    # Add vertex to the graph.
    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    # Not magic func, returns the vertex if in vertList.
    def getVertex(self,key):
        return self.vertList[key]
    
    # Magic func, checks if key in vertList.
    def __contains__(self,key):
        return key in self.vertList
    
    # Adds two vertices to graph and directs one to the other.
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nt = self.addVertex(t)
        
        self.vertList[f].addNeighbor(self.vertList[t],cost)
    
    # Returns all vertices in graph.
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
    
# NOTE: For the future
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
