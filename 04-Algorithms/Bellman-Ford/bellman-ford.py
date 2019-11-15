"""
    Bellman-Ford Algorithm implementation.

    There are two graphs provided in the source
    file. Uncomment the second one for a negative
    cycled graph.
"""

import sys

__author__ = "Rafael Broseghini"

GRAPH = {
    "a": {"b": 7, "c": 3},
    "b": {"a": 7, "c": 1, "d": 2},
    "c": {"a": 3, "b": 1, "d": 2},
    "d": {"b": 2, "c": 2, "e": 4},
    "e": {"b": 6, "d": 4},
}

# GRAPH = {
#     "a": {"b":-1, "c":4},
#     "b": {"c":3, "d":2, "e":-2},
#     "c": {},
#     "d": {"b":-1, "c":5},
#     "e": {"b":6, "d":-3}
# }


def bellmanFord(graph, source):
    dist = {k: sys.maxsize for k in graph}
    dist[source] = 0
    for i in range(len(graph) - 1):
        for v in graph:
            for n in graph[v]:
                if (dist[v] + graph[v][n]) < dist[n]:
                    dist[n] = dist[v] + graph[v][n]

    for i in range(len(graph) - 1):
        for v in graph:
            for n in graph[v]:
                if (dist[v] + graph[v][n]) < dist[n]:
                    return "Graph contains negative weight cycle"
    return dist


if __name__ == "__main__":
    for k in GRAPH:
        print(bellmanFord(GRAPH, k))
