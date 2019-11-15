"""
Python script that returns the maximum
number of paths from the top left to
the bottom right of a grid with only
'Down' and 'Right' movement allowed.

Input: n m
n -> number of rows
m -> number of columns
"""


def check_bound(x, y, n, m):
    if x < n and y < m:
        return True
    return False


# Direction of neighbor logic goes here.
# We get right and bottom neighbors here.
# If we want to get top and left neighbors
# There needs to be a little more checking
# in the check bound logic function.
def get_neighbors(x, y, n, m):
    neigh = []
    if check_bound(x + 1, y, n, m):
        neigh.insert(0, (x + 1, y))
    if check_bound(x, y + 1, n, m):
        neigh.insert(0, (x, y + 1))
    return neigh


def num_paths(n: int, m: int) -> int:
    target = (n - 1, m - 1)
    queue = [(0, 0)]
    count = 0
    while len(queue) > 0:
        x, y = queue.pop()
        if (x, y) == target:
            count += 1
        neigh = get_neighbors(x, y, n, m)
        queue.extend(neigh)

    return count


def main():
    n = 8
    m = 3
    print(num_paths(n, m))


if __name__ == "__main__":
    main()

