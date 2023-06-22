class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}
        
        #Number of stones alice gets
        def dfs(alice,i,M):
            if i == len(piles):
                return 0
            if (alice,i,M) in cache:
                return cache[(alice,i,M)]
            
            res = 0 if alice else float('inf')
            prefix_sum = 0
            for x in range(1, 2 * M + 1):
                
                if i + x  > len(piles): #if its out of bounds
                    break
                prefix_sum += piles[i + x - 1]
                if alice:
                    res = max(res, prefix_sum + dfs(not alice, i + x ,max(M,x)))
                else:
                    res = min(res, dfs(not alice,i + x,max(M,x)))
            cache[(alice,i,M)] = res
            return res
        
        return dfs(True,0,1)
        