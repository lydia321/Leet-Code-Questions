class Solution:
    def timeRequiredToBuy(self, ticket: List[int], k: int) -> int:
        count = 0
        i = 0
        
        while ticket[k]>0:
            if ticket[i] > 0:
                ticket[i] -= 1
                count += 1
            i = (i+1)%len(ticket) # cleaver for loop
        return count     
                
            
            
            
        
        
        