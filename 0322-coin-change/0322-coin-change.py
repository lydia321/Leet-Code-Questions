class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        
        def dp(i,target):
            
            if (i,target) in cache:
                return cache[(i,target)]
            if target == 0:
                return 0
            if i == len(coins) or target < 0:
                return amount + 1

            cache[(i,target)] = min(dp(i + 1,target),dp(i,target - coins[i]) + 1)
            return cache[(i,target)]
        res = dp(0,amount)
        return res if res != amount + 1 else -1
