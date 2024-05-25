# Leetcode 2824. Count Pairs Whose Sum is Less than Target

def countPairs(nums, target):
    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < target:
                count += 1
    return count


if __name__ == '__main__':
    print(countPairs([-1, 1, 2, 3, 1], 2))  # test case 1
    print(countPairs([-6, 2, 5, -2, -7, -1, 3], -2))  # test case 2
