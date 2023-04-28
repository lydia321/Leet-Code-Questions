class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def dp(i,total):
            if i < 0 and total == target:
                return 1
            if i < 0:
                return 0
            if (i,total) in cache:
                return cache[(i,total)]
            pos = dp(i - 1, total + nums[i])
            neg = dp(i - 1, total - nums[i])
            cache[(i,total)] = pos + neg
            return pos + neg
        
        return dp(len(nums)-1,0)
      