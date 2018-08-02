#!/usr/bin/env python

import sys
from graph import Graph, Vertex

""" 
Implementation of the Word Ladder Algorithm
using Breadth First Search on a Graph.
"""

def buildGraph(g):
    d = {}
    with open("words.txt") as file:
        for word in file:
            word = word.replace("\n","")
            for i in range(len(word)):
                bucket = word[:i] + "_" + word[i+1:]
                if bucket not in d:
                    d[bucket] = [word]
                else:
                    d[bucket].append(word)

    for vertex in d.keys():
        for word in d[vertex]:
            for word2 in d[vertex]:
                if word != word2:
                    g.addEdge(word,word2)
    return g

def BFS(g, start, goal):
    visited = set() 
    queue = [start]
    visited.add(start)
    while len(queue) > 0:
        currentVert = queue.pop()
        visited.add(currentVert)
        for nbr in g[currentVert].getConnections():
            if nbr not in visited:
                g[nbr].setDistance(g[currentVert].getDistance() + 1)
                g[nbr].setPred(g[currentVert])
                visited.add(nbr)
                queue.insert(0,nbr)
    return visited

def traverse(g, start, goal):
    bfs = BFS(g,start, goal)
    path = []
    pred = g[goal].getPred()
    if start in bfs and goal in bfs:
        path.append(g[goal])
        while pred != None:
            path.append(pred)
            pred = pred.getPred()
    return reversed(path)

def main():
    GRAPH = Graph()
    g = buildGraph(GRAPH)
    print("Breadth First Search Word Ladder Algorithm!")
    print("="*43+"\n")

    try:
        a, b = input("Choose word1: "), input("Choose word2: ")
        b = traverse(g, a, b)
        print("\nPATH:")
        for v in b:
            print(v.id)
    except Exception as err:
        print("\nERROR: Cannot reach '{}' from start: '{}' based on our words.txt file.".format(b, a))


if __name__ == '__main__':
    main()
