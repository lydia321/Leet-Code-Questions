class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        m=max(candies)
        output=[]
        for i in candies:
                if i + extraCandies >= m:
                    output.append(True)
                else:
                    output.append(False)
        return output            
                
                
        
        