# Leetcode: 1351. Count Negative Numbers in a Sorted Matrix

def countNegatives(grid):
    count = 0
    for col in grid:
        for row in col:
            if row < 0:
                count += 1
    return count


if __name__ == '__main__':
    print(countNegatives([[3, 2], [1, 0]]))
    print(countNegatives([[4, 3, 2, -1],
                          [3, 2, 1, -1],
                          [1, 1, -1, -2],
                          [-1, -1, -2, -3]]))
