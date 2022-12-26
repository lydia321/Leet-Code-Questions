class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,suffix = [1],[1]
        s = nums[::-1] 
        res = []
        
        for i in range(len(nums)-1):
            prefix.append(prefix[-1]*nums[i])
        
        for i in range(len(s)-1):
            suffix.append(suffix[-1]*s[i])
       
        suffix = suffix[::-1]
       
        for i in range(len(suffix)):
            res.append(prefix[i]*suffix[i])
            
        return res