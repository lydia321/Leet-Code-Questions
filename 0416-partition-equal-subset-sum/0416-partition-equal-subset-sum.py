class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        target = sum(nums)//2
        cache = {}
        def dp(i,total):
            if (i,total) in cache:
                return cache[(i,total)]
            if total == 0:
                return True
            if total < 0 or i == len(nums):
                return False
            
            cache[(i,total)] = dp(i + 1, total - nums[i]) or dp(i + 1, total)
            return cache[(i,total)]
            
        
        return dp(0,target)
       