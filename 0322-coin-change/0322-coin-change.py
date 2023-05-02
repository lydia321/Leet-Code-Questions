class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        Descions: 
        1) we use the coin and increase our count and choose between all coins
        2) we dont chose the coin, count is the same and choose between the rest of the coins
        
        '''
    
        cache = {}
        def dp(i,target):
            nonlocal res
            if (i,target) in cache:
                return cache[(i,target)]
            if target == 0:
                return 0
            if target < 0 or i == len(coins): #invalid case
                return inf
            cache[(i,target)] = min(dp(i+1,target), dp(i,target - coins[i]) + 1)
            return cache[(i,target)]
        
        res = dp(0,amount)
        return res if res != inf else -1
            
            
            