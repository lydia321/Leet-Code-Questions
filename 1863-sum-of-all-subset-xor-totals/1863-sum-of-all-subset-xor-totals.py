class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i,curr):
            if i == len(nums):
                return curr
            if (i,curr) in cache:
                return cache[(i,curr)]
            skip = dfs(i + 1, curr)
            keep = dfs(i + 1, curr ^ nums[i]) 
            cache[(i,curr)] = skip + keep
            return cache[(i,curr)]
            
        return dfs(0,0)