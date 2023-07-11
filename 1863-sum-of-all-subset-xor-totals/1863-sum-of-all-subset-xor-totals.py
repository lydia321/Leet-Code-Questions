class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i,curr):
            if i == len(nums):
                return curr
            if (i,curr) in cache:
                return cache[(i,curr)]
            cache[(i,curr)] = dfs(i + 1, curr ^ nums[i]) + dfs(i + 1, curr )
            return cache[(i,curr)]
            
        return dfs(0,0)