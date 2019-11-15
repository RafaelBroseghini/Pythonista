import heapq
import requests


class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        if not isinstance(other, Node):
            raise ValueError("Can only compare to Node class")
        return self.f < other.f

    def __gt__(self, other):
        if not isinstance(other, Node):
            raise ValueError("Can only compare to Node class")
        return self.f > other.f


def mhd(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def get_neighbors(graph: list, coord: list):
    neighbors = []
    append_neighbors(coord[0] - 1, coord[1], graph, neighbors)
    append_neighbors(coord[0] + 1, coord[1], graph, neighbors)
    append_neighbors(coord[0], coord[1] - 1, graph, neighbors)
    append_neighbors(coord[0], coord[1] + 1, graph, neighbors)

    return neighbors


def append_neighbors(x: int, y: int, graph: list, array: list):
    if y >= 0 and y <= len(graph) - 1 and x >= 0 and x <= len(graph[0]) - 1:
        if graph[y][x] != "X":
            array.append([x, y])


def astar(maze, start, target):
    start = Node(None, start)
    target = Node(None, target)
    open_list, open_set, closed_set = [], set(), set()

    heapq.heappush(open_list, start)
    open_set.add(tuple(start.position))

    while len(open_list) > 0:
        current = heapq.heappop(open_list)

        if current == target:
            path = []
            c = current
            while c is not None:
                path.append(c.position)
                c = c.parent
            return path[::-1]

        neighbors = get_neighbors(maze, current.position)

        for c in neighbors:
            child = Node(current, c)

            if tuple(child.position) in closed_set:
                continue

            child.g = current.g + 1
            child.h = mhd(target.position, child.position)
            child.f = child.g + child.h

            if tuple(child.position) in open_set:
                continue

            for open_node in open_list:
                if child == open_node and child.f > open_node.f:
                    continue

            open_list.append(child)
            open_set.add(tuple(child.position))
            closed_set.add(tuple(current.position))


def directions(curr: list, previous: list, dirs: list) -> list:
    if curr[1] == previous[1]:
        if previous[0] > curr[0]:
            dirs.append("W")
        else:
            dirs.append("E")
    elif curr[0] == previous[0]:
        if previous[1] < curr[1]:
            dirs.append("S")
        else:
            dirs.append("N")

    return dirs


def get(url: str) -> dict:
    res = requests.get(url)
    return res.json()


def build_uri(path: str) -> str:
    return "https://api.noopschallenge.com" + path


def main() -> None:
    uri = "/mazebot/race/start"

    start = requests.post(build_uri(uri), json={"login": "RafaelBroseghini"}).json()
    maze_path = start["nextMaze"]

    finished = False

    while not finished:
        data = get(build_uri(maze_path))

        maze, answer = data["map"], data["mazePath"]

        source, target = data["startingPosition"], data["endingPosition"]

        res = astar(maze, source, target)

        dirs = []
        for i in range(len(res) - 1, 0, -1):
            dirs = directions(res[i], res[i - 1], dirs)

        dirs = "".join(dirs[::-1])

        r = requests.post(
            "https://api.noopschallenge.com" + answer, json={"directions": dirs}
        ).json()

        print(r)
        if r["result"] == "success":
            maze_path = r["nextMaze"]
        else:
            finished = True


if __name__ == "__main__":
    main()
