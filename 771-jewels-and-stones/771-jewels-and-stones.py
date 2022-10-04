class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        lookup={}
        for j in jewels:
            lookup[j]=1
        
        count=0
        for s in stones:
            if lookup.get(s) != None:
                count+=1
        return count        