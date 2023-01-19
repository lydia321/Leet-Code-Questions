class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1 = [0,nums[0]]
        dp2 = [0,nums[1]]
        
        for i in range(1,len(nums)-1):
            curr = max((nums[i] + dp1[-2]),(dp1[-1]))
            dp1.append(curr)
        for i in range(2,len(nums)):
            curr = max((nums[i]+dp2[-2]),dp2[-1])
            dp2.append(curr)
        return max(max(dp1),max(dp2))
                       
                