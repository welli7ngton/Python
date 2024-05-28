def maximumCount(nums):
    neg, pos = 0, 0
    for x in nums:
        if x > 0 and x != 0:
            pos += 1
        elif x < 0 and x != 0:
            neg += 1
    return max(neg, pos)


if __name__ == '__main__':
    print(maximumCount([-3, -2, -1, 0, 0, 1, 2]))
