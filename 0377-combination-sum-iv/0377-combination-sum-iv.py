class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        cache = {}
        
        def dfs(curr):
            
            if curr == 0:
                return 1
            
            if curr < 0: return 0
            
            if curr in cache: return cache[curr]
            
            cache[curr] = 0
            
            for num in nums:
                if curr - num < 0: break
                cache[curr] += dfs(curr-num)
            
            return cache[curr]
        
        return dfs(target)