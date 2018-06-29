def binSearch(arr, elem):
    first = 0
    last = len(arr) - 1
    found = False
    
    while first <= last and not found:
        middle = (first+last) // 2
        if elem == arr[middle]:
            found = True
        else:
            if arr[middle] < elem:
                first = middle + 1
            elif arr[middle] > elem:
                last = middle - 1
    return found

'''Recursive Binary Search'''
def rec_bin_search(arr,elem):
    # Base case.
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2

        if arr[mid] == elem:
            return True
        else:
            if elem > arr[mid]:
                rec_bin_search(arr[mid+1:],elem)
            elif elem < arr[mid]:
                rec_bin_search(arr[:mid], elem)


def main():
    arr = [1,2,3,4,5,6,7,8]
    print("Using Sequential Binary Search: \n")
    print("Looking for elem {} in {}: {}".format(9,arr,binSearch(arr,9)))
    print("Looking for elem {} in {}: {}".format(3,arr,binSearch(arr,3)))

    print("\nUsing Recursive Binary Search: \n")
    print("Looking for elem {} in {}: {}".format(9,arr,binSearch(arr,9)))
    print("Looking for elem {} in {}: {}".format(3,arr,binSearch(arr,3)))

if __name__ == "__main__":
    main()
