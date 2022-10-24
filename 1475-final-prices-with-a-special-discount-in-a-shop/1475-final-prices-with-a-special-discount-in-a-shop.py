class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[]
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    ans.append(abs(prices[i]-prices[j]))
                    break
            else:
                ans.append(prices[i])
           
        ans.append(prices[-1])
        return ans