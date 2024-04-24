class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        cache = {}
        
        def dfs(i,Bool):
            if i == len(nums):
                return 0
            if (i,Bool) in cache:
                return cache[(i,Bool)]
            temp = nums[i]%2 == 0 
            if temp == Bool:
                cache[(i,Bool)] = nums[i] + dfs(i+1,Bool)
            else:
                cache[(i,Bool)] = max(dfs(i+1,not Bool) + nums[i] - x, dfs(i+1, Bool))
            
            return cache[(i,Bool)]
        
        return dfs(0,nums[0]%2 == 0)