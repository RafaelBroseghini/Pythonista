#!/usr/bin/env python

"""
Kevin Bacon number algorithm, using
Breadth First Search and command line
arguments.
"""

import sys
from graph import Graph
from vertex import Vertex

def build_graph(filename):
  g = Graph()
  movie_dict = {}

  with open(filename, "r+") as infile:
    for line in infile:
      line = line.split("|")
      movie = line[0]
      actor = line[1].replace("\n","").replace("\t","")

      if movie in movie_dict:
        movie_dict[movie].append(actor)
      else:
        movie_dict[movie] = [actor]


  for movie in movie_dict:
    for actor in movie_dict[movie]:
      for actor2 in movie_dict[movie]:
        if actor != actor2:
          g.addEdge(actor, actor2, movie)

  return g

def bfs(graph, start):
  graph[start].setPred("No one")
  queue = [start]
  while len(queue) > 0:
    current = queue.pop()
    for item in graph[current].getConnections():
      if graph[item].color == "white":
        graph[item].color = "gray"
        graph[item].setPred(current)
        queue.insert(0, item)
    
def traverse(graph, x, goal):
  path = []
  dis = 0
  path.append(x)
  while graph[x].getPred() != None:
    pred = graph[x].getPred()
    path.append(pred)
    x = graph[x].getPred()
    dis += 1

    if x == goal:
      return path
  return "Oops, no Kevin Bacon number for {}".format(x)


GRAPH = build_graph("movies.txt")

def main():
  bfs(GRAPH, "Kevin Bacon")
  inp = input("Enter name of actor/actress (exit to stop) for their Kevin Bacon number: ")


  while inp != "exit":
    if inp == "Kevin Bacon":
      print("0 of course!")
    else:
      result = traverse(GRAPH, inp, "Kevin Bacon")
      print("{}'s Kevin Bacon numbers is: {}".format(inp, len(result)))
      for actor in range(len(result)-1):
        pred = GRAPH[result[actor]].getPred()
        movie_in_common = GRAPH[result[actor]][pred]
        print("{} acted with {} in {}".format(result[actor], pred, movie_in_common))


    inp = input("Enter name of actor/actress (exit to stop) for their Kevin Bacon number:")

if __name__ == "__main__":
  main()
