class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        
        res = 0
        l = 0
        currP = 1
        
        for r in range(len(nums)):
            currP *= nums[r]
            
            while currP >= k:
                currP = currP//nums[l]
                l += 1
            res += r-l+1
               
        return res
            
        