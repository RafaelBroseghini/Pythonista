import sys
import inspect

"""
    Note: 
    
    This algorithm would be extremely useful if we 
    compute it once for every node as the starting 
    node and save it to a database. 
    
    This would save us computing time if we needed to  
    look up at the results in the database instead of 
    having to run the program every time.

    Although we must be aware that if something changes 
    in the graph, re running the program is a must, as 
    we do not want outdated information when populating 
    the database.

"""



# Digraph
graph = {
    "a": {"b":7, "c":3},
    "b": {"a":7, "c":1, "d":2},
    "c": {"a":3, "b":1, "d":2},
    "d": {"b":2, "c":2, "e":4},
    "e": {"b":6, "d":4}
}

# Method that finds neighbor with smallest distance.
def get_min_nbr(key, visited):
    minNbr_value = sys.maxsize
    for nbr in graph[key]: 
        if graph[key][nbr] < minNbr_value and nbr not in visited:
            minNbr_value = graph[key][nbr]
            minNbr = nbr

    return minNbr



def djikstra(graph, source, target):
    unvisited = [k for k in graph.keys()]
    visited   = []
    distances = {k: sys.maxsize for k in graph.keys()}
    predecessors = {k: "" for k in graph.keys()}
    distances[source] = 0

    current = source
    # Until both visited and unvisited arrays are not the
    # same, we keep visiting nodes.
    while visited != unvisited:
        visited.append(current)
        distance = distances[current]
        for nbr in graph[current]:
            # NOTE: Here we check if current distance is less than
            # previously know distance. If True, we set distance to current distance.
            if graph[current][nbr] + distance < distances[nbr]:
                distances[nbr]     = graph[current][nbr] + distance
                predecessors[nbr]  = current

        # NOTE: I will refactor code and figure out a way to return false if cannot reach target.
        try:
            current = get_min_nbr(current, visited)
        except:
            return distances, predecessors
            # return "Shortest path from {} to {} is: {}".format(source, target, distances[target])


def get_shortest_path(source, target):
    # Unpack dijkstra function, since it returns a tuple.
    distances, predecessors = djikstra(graph, source, target)
    current = target
    path = []
    # Get predecessors from target backwards.
    while current != source:
        path.insert(0, current)
        current = predecessors[current]
    path.insert(0, current)

    return distances[target], path

# Save source, target, distance, path to a file for lookup.
# This avoids having to compile the program everytime we
# need to find the shortest path from/to a new node.

def save_to_file():
    # All vertexes in the graph.
    nodes = [k for k in graph.keys()]
    with open("graph_lookup.txt","w+") as file:
        file.write("{:<10} {:<10} {:<10} {:<10}\n".format("SOURCE", "TARGET", "DISTANCE", "PATH"))

        for v in nodes:
            for j in nodes:
                # Here we check if nodes aren't the same. Distance is 0 from node to itself.
                if v != j:
                    res = get_shortest_path(v, j)
                    file.write("{:<10} {:<10} {:<10} {:<10}\n".format(v, j, res[0], str(res[1])))



def main():
    save_to_file()
    # print(get_shortest_path("a","e"))

if __name__ == '__main__':
    main()