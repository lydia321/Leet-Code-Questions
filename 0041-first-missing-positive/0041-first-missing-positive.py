class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        nums = set(nums)
        for i in nums:
            if res in nums:
                res += 1
            else:
                return res
        return  res