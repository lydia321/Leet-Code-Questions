class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = 1
        m = 0
        
        while len(prices) > 1 and sell < len(prices):
            
            if prices[sell]>prices[buy]:
                diff = prices[sell]-prices[buy]
                m = max(m,diff)
                
            else:
                buy = sell
            sell += 1    
                
           
        return m
        
        