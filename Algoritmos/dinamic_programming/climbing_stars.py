# Leetcode: 70. Climbing Stairs

def climbStairs(n):
    if n < 3:
        return n

    prev1, prev2, curr = 1, 1, 0

    while n > 1:
        curr = (prev1 + prev2)
        prev1 = prev2
        prev2 = curr
        n -= 1

    return curr


if __name__ == '__main__':
    print(climbStairs(5))
