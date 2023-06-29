class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            curr_max = nums[i]
            curr_min = nums[i]
            for j in range(i + 1,len(nums)):
                curr_max = max(curr_max,nums[j])
                curr_min = min(curr_min,nums[j])
                res += curr_max - curr_min
        return res
                