class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        MaxSub = max(nums)
        currMin,currMax = 1,1
        
        for n in nums:
            if n == 0:
                 currMin,currMax = 1,1
            temp = currMax
            currMax = max(currMin*n,currMax*n,n)
            currMin = min(currMin*n,temp*n,n)
            
            MaxSub = max(MaxSub,currMax,currMin)
            
        return MaxSub
            
        
        