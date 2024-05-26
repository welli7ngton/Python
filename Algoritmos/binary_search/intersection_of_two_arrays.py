# Leetcode: 349. Intersection of Two Arrays

def intersection(nums1, nums2):
    intersection = []

    for x in range((max(len(nums1), len(nums2)))):
        try:
            if nums1[x] in nums2 and nums1[x] not in intersection:
                intersection.append(nums1[x])
        except IndexError:
            pass

    return intersection


if __name__ == '__main__':
    # print(intersection([1, 2, 2, 1], [2, 2]))
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
