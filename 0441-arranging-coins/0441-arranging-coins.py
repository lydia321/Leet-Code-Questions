class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = n
        
        while l <= r:
            m = (l+r)//2
            
            Coins_we_need = (m/2)*(m + 1)
            if Coins_we_need == n:
                return m
            elif Coins_we_need > n:
                r = m - 1
            else:
                l = m + 1
        return r
                