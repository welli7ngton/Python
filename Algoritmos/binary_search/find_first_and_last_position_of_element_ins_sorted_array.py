# Leetcode: 34. Find First and Last Position of Element in Sorted Array


def searchRange(nums, target):
    left = 0
    right = len(nums) - 1
    result = [-1, -1]

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            result[0] = mid
            result[1] = mid
            # Expandindo para a esquerda
            while result[0] > 0 and nums[result[0] - 1] == target:
                result[0] -= 1
            # Expandindo para a direita
            while result[1] < len(nums) - 1 and nums[result[1] + 1] == target:
                result[1] += 1
            return result
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


if __name__ == '__main__':
    print(searchRange([5, 7, 7, 8, 8, 10], 8))
    print(searchRange([1], 1))
