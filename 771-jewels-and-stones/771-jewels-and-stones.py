class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        lookup={}
        count= 0 
        
        for i in jewels:
            lookup[i]=1
            
        for s in stones:
            if lookup.get(s) != None:
                count+=1
                
        return count        
            