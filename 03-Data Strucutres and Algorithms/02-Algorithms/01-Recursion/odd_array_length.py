# Determine whether the length of an array is odd.

def odd_length_slice(arr: list) -> bool:
    if len(arr) == 0:
        return False
    elif len(arr) == 1:
        return True
    return odd_length_slice(arr[2:])


def odd_length_reference(arr: list, n: int) -> bool:
    if n == 0:
        return False
    elif n == 1:
        return True
    return odd_length_reference(arr, n-2)

if __name__ == "__main__":
    print(odd_length_slice([1,2,3,4,5]))
    print(odd_length_slice([1,2,3,4,5,6,7,8]))
    print(odd_length_reference([1,2,3,4,5],5))
    print(odd_length_reference([1,2,3,4,5,6,7,8],8))