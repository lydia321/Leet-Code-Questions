class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        
        dp = [nums[-1]]
        cache[nums[-1]] = 1
        
        for i in range(len(nums)-2,-1,-1):
            val = 1
            for each in dp:
                if nums[i] < each:
                    val = max(val,cache[each] + 1)
            cache[nums[i]] = val
            dp.append(nums[i])
        res = 0
        for val,count in cache.items():
            res = max(res,count)
        return res
            