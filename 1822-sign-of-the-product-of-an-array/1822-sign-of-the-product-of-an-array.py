class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 0
        
        for i in nums:
            if i < 0:
                p += 1
            elif i == 0:
                return 0
                break    
        if p %2 == 0:
            return 1
        return -1
                
            
        