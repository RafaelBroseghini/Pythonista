'''Unordered Array'''
def seq_search(arr,elem):
    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == elem:
            found = True
        pos += 1
    return found



arr = [1,2,3,4,5,6,7,8,9,10]

print(seq_search(arr,5))


'''Ordered Array'''
def seq_search_ordered(arr,elem):
    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not stopped:
        if arr[pos] > elem:
            stopped = True
        elif arr[pos] == elem:
            found = True
            stopped = True
        pos += 1

    return found

lst = [33,44,56,189,999,1234,55442,888998]

print(seq_search_ordered(lst,1235))
