class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        Descions:
        1) you can use the coin,choose between all coins 
        2) dont use the coin, choose between the remaining coins
        '''
        cache = {}
        def dp(i,target):
            if (i,target) in cache:
                return cache[(i,target)]
            if target == 0:
                return 1
            if target < 0 or i == len(coins):
                return 0
            cache[(i,target)] = dp(i,target - coins[i]) +  dp(i + 1, target)
            return cache[(i,target)]
            
        return dp(0,amount)
