class Vertex(object):
  def __init__(self, data):
    self.key = data
    self.connectedTo = {}
    self.pred = None
    self.color = "white"
  
  def getKey(self):
    return self.key
  
  def getPred(self):
    return self.pred

  def setPred(self, p):
    self.pred = p
  
  def getConnections(self):
    return [key for key in self.connectedTo.keys()]
  
  def addNeighbor(self, nbr, weight=0):
    self.connectedTo[nbr] = weight

  def __getitem__(self, key):
    return self.connectedTo[key]

  def __str__(self):
    return "{}: {}".format(self.key, self.connectedTo)
