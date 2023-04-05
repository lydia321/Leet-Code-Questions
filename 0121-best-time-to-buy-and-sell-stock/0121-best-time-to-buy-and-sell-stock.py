class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [prices[0]]
        res = 0
        for i in range(1,len(prices)):
            if prices[i] <= dp[-1]:
                dp.pop()
                dp.append(prices[i])
            else:
                res = max(res,(prices[i] - dp[0]))
        # print(stack)
        return res
            
        
        
