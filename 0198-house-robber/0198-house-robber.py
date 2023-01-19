class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0,nums[0]]
        
        for i in range(1,len(nums)):
            curr = max((nums[i] + dp[-2]),(dp[-1]))
            dp.append(curr)
        return max(dp)
                             
        