class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        val = float('inf')
        
        while l <= r:
            k = (l + r)//2
            res = 0
            for i in piles:
                res += math.ceil(i/k)#Round up
            
            if res <= h:
                val = min(val,k)
                r = k - 1
            else:
                l = k + 1
                
        return val
            
            
            
        
        
        
        
        
        
        