class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0,nums[-1]]
        
        for i in range(len(nums) - 2, - 1, - 1):
            dp.append(max(nums[i] + dp[-2], dp[-1]))
        return max(dp)