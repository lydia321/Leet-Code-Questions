class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = []
        
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                
                if prices[i] >= prices[j]:
                    output.append(prices[i]-prices[j])
                    break
                    
            else:
                output.append(prices[i])
        output.append(prices[-1])
        return output
                    
                    
        