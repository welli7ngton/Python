def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            high = mid - 1
        else:
            low == mid + 1
    return None


if __name__ == '__main__':
    print([1, 3, 5, 7, 9], 3)
