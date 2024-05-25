# Leetcode 2824. Count Pairs Whose Sum is Less than Target
# O(n^2): Brute force
# def countPairs(nums, target):
#     count = 0

#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] < target:
#                 count += 1
#     return count

# O(n log n): Two Pointers
def countPairs(nums, target):
    nums.sort()  # Ordena o array para usar two pointers
    count = 0
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            # Se a soma dos números for menor que o alvo,
            # todos os números entre left e right também
            # formarão pares com right, então adicionamos
            # a diferença entre right e left ao contador.
            count += right - left
            left += 1
        else:
            # Se a soma dos números for maior ou igual ao alvo,
            # decrementamos o ponteiro right.
            right -= 1

    return count


if __name__ == '__main__':
    print(countPairs([-1, 1, 2, 3, 1], 2))  # test case 1
    # print(countPairs([-6, 2, 5, -2, -7, -1, 3], -2))  # test case 2
