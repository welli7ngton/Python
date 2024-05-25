# Leetcode: 2089. Find Target Indices After Sorting Array
def targetIndices(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if nums[i] == target:
            result.append(i)
    return result


if __name__ == '__main__':
    print(targetIndices([1, 2, 5, 2, 3], 2))
    print(targetIndices([1, 2, 5, 2, 3], 3))
    print(targetIndices([1, 2, 5, 2, 3], 5))
