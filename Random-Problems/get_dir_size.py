import os


def get_size_dir_bfs(pwd):
    queue = []
    queue.insert(0, pwd)
    
    total = os.path.getsize(pwd)
    while len(queue) > 0:
        curr_path = queue.pop()
        list_dir = os.listdir(curr_path)

        for p in list_dir:
            full_path = os.path.join(curr_path, p)
            if os.path.isdir(full_path):
                queue.insert(0, full_path)
            total += os.path.getsize(full_path)
    
    return total


def get_size_dir_dfs(pwd):
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
def get_size_dir_recursive(pwd):
    total = os.path.getsize(pwd)

    if os.path.isdir(pwd):
        for p in os.listdir(pwd):
            child_path = os.path.join(pwd, p)
            total = total + get_size_dir_recursive(child_path)
    
    return total


def main():
    inp = input("Full directory path: ")
    print("The cumulative disk space of {} is: {} bytes".format(inp, get_size_dir_bfs(inp)))
    print("The cumulative disk space of {} is: {} bytes".format(inp, get_size_dir_dfs(inp)))
    print("The cumulative disk space of {} is: {} bytes".format(inp, get_size_dir_recursive(inp)))

if __name__ == '__main__':
    main()