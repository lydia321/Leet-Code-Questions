class Solution:
    def numSquares(self, n: int) -> int:
        lookup = []
        for i in range(101):
            lookup.append((i)**2)
        
        dp = [n] * (n + 1)
        dp[0] = 0
        
        for a in range(1, n + 1):
            
            for i in range(a):   
                curr = lookup[i]
                if a - curr >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - curr])
                else:
                    break
                    
        return dp[n]
    '''
    12 [0,1,12..]
    
    1 - 13
        1,2 -> 
    
    '''