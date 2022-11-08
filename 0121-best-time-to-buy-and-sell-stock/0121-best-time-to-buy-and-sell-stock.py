class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        m = 0
        
        for sell in range(1,len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                diff = prices[sell] - prices[buy]
                m = max(m, diff)
                     
        return m
        
        