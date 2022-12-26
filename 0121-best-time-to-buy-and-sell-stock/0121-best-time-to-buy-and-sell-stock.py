class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        curr = 0
        
        while r < len(prices):
            curr = max(curr,prices[r] - prices[l])
            
            if prices[r] < prices[l]:
                l = r
            r += 1
        return curr
        
        
        