def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    count = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return None, count


if __name__ == '__main__':
    print(binary_search([n for n in range(0, 128)], 128))
