import heapq
import sys

g = [
  [0,0,0,0,0],
  [1,1,0,0,0],
  [0,0,0,0,1],
  [1,1,1,0,0],
  [1,0,0,0,1],
  [0,0,1,1,1],
  [0,1,1,1,1]
]

drawing = [["0" for i in range(len(g[0]))] for i in range(len(g))]

class Item(object):
  def __init__(self, coord, distance):
        self.coord = coord
        self.distance = distance
  
  def __lt__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Can only compare to Item class")
        return self.distance < other.distance

  def __gt__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Can only compare to Item class")      
        return self.distance > other.distance

def mhd(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def append_neighbors(x: int, y: int, graph: list, array:list):
    if x >= 0 and x <= len(graph)-1 and y >= 0 and y <= len(graph[0])-1:
        if graph[x][y]!= 1:
            array.append([x, y])

def get_neighbors(graph: list, coord: list):
    neighbors = []
    append_neighbors(coord[0]-1, coord[1], graph, neighbors)
    append_neighbors(coord[0]+1, coord[1], graph, neighbors)
    append_neighbors(coord[0], coord[1]-1, graph, neighbors)
    append_neighbors(coord[0], coord[1]+1, graph, neighbors)
    return neighbors

def draw_path(x: int, y: int, source: list, goal: list, path: list):
    drawing = [[" " for i in range(x)] for j in range(y)]
    x_source, y_source = source[0], source[1]
    x_goal, y_goal = goal[0], goal[1]
    step = 0
    for coord in path:
        x, y = coord[0], coord[1]
        # drawing[x][y] = f"{step}"
        # or
        drawing[x][y] = "X"
        step += 1
    drawing[x_source][y_source] = "S"
    drawing[x_goal][y_goal] = "T"

    for line in drawing:
        print(" ".join(line))

def best_first_search(graph, source, goal):
    visited, unvisited, path = set(), [], []
    heapq.heappush(unvisited,Item(source, 0))
    while len(unvisited) > 0:
        curr = heapq.heappop(unvisited)
        path.append(curr.coord)
        if curr.coord == goal:
            return path
        visited.add(tuple(curr.coord))
        neighbors = get_neighbors(graph, curr.coord)
        for n in neighbors:
            if tuple(n) not in visited:
                dis = mhd(n, goal)
                heapq.heappush(unvisited, Item(n, dis))
    return []

def main():
    source, target = [0,0], [6,0]
    path = best_first_search(g, source, target)
    if len(path) > 0:
        for line in g:
            print(" ".join(str(x) for x in line))
        print() 
        draw_path(len(g[0]), len(g), source, target, path)


if __name__ == "__main__":
    main()


