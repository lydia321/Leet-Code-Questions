class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        res = [1]
        rnums = nums[::-1]
        for i in range(len(rnums)-1):
            res.append(res[-1]*rnums[i])
        res = res[::-1]
          
        pos = 1 
        for i in range(len(nums)):
            res[i] *= pos
            pos *= nums[i]
        return res
            
        
        
   