class Solution:
    def timeRequiredToBuy(self, ticket: List[int], k: int) -> int:
        curr = 0
        
        for i in range(k+1): 
            curr += min(ticket[i], ticket[k])
        for i in range(k+1,len(ticket)):
            curr += min(ticket[i], ticket[k]-1)
        return curr        
            
        