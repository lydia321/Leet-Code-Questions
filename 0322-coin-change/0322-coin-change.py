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
            res = dp(i + 1,target)
            if target >= coins[i]:
                res = min(res,dp(i,target - coins[i]) + 1)
            cache[(i,target)] = res
            return cache[(i,target)]
        res = dp(0,amount)
        return res if res != amount + 1 else -1
