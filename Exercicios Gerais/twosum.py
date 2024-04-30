class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for cur in range(len(nums)):
            complement = target - nums[cur]
            if complement in hashmap:
                return [cur, hashmap[complement]]
            hashmap[nums[cur]] = cur


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 5, 5, 11], 10))
