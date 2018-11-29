"""
Script to get cumulative disk usage size 
in bytes of path passed in as argument 
and all its children.

I originally did this with three different 
implementations:
    Breadth First Search.
    Depth First Search.
    Recursive.
"""

import os

__author__ = "Rafael Broseghini"

def get_size_dir_bfs(pwd: str) -> int:
    queue = []
    queue.insert(0, pwd)
    
    total = os.path.getsize(pwd)
    while len(queue) > 0:
        curr_path, list_dir = queue.pop(), os.listdir(curr_path)

        for p in list_dir:
            full_path = os.path.join(curr_path, p)
            if os.path.isdir(full_path):
                queue.insert(0, full_path)
            total += os.path.getsize(full_path)
    
    return total


def get_size_dir_dfs(pwd: str) -> int:
    stack = []

    stack.append(pwd)
    
    total = os.path.getsize(pwd)
    while len(stack) > 0:
        curr_path = stack.pop()

        for p in os.listdir(curr_path):
            full_path = os.path.join(curr_path, p)
            if os.path.isdir(full_path):
                stack.append(full_path)
            total += os.path.getsize(full_path)

    return total

# Recursive implementation.
def get_size_dir_recursive(pwd: str) -> int:
    total = os.path.getsize(pwd)

    if os.path.isdir(pwd):
        for p in os.listdir(pwd):
            child_path = os.path.join(pwd, p)
            total = total + get_size_dir_recursive(child_path)
    
    return total


def main():
    inp = input("Full directory path: ")
    print("Breadth First Search cumulative disk usage size of {} is: {} bytes".format(inp, get_size_dir_bfs(inp)))
    print("Depth First Search cumulative disk usage size of {} is: {} bytes".format(inp, get_size_dir_dfs(inp)))
    print("Recursive cumulative disk usage size of {} is: {} bytes".format(inp, get_size_dir_recursive(inp)))
if __name__ == '__main__':
    main()
