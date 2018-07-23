def binarySearch(lst, value):
    found = False
    i = len(lst) // 2

    while not found and i > 0:
        i = len(lst) // 2
        if value < lst[i]:
            lst = lst[:i]
        elif value > lst[i]:
            lst = lst[i+1:]
        else:
            found = True

    return found

def main():
    lst = [1,2,3,4,5,6,7,8,9,10,11]
    print(binarySearch(lst,6))
if __name__ == '__main__':
    main()