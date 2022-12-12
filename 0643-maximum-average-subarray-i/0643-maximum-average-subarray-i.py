class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        res = curr/k
        
        l = 0
        
        for r in range(k,len(nums)):
           
            curr += nums[r]
            curr -= nums[l]
            
            res = max(res,(curr/k))
            l += 1
        return res
        
            
            
        
        
        