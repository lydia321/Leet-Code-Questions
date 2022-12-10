class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        maxAverage = curr/k
        l = 0
        
        for r in range(k,len(nums)):
            curr -= nums[l]
            curr += nums[r]
            maxAverage = max(maxAverage,curr/k)
            l += 1
        return maxAverage
            
            
        
        
        