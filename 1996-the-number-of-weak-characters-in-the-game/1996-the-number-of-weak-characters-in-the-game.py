class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x:(-x[0],x[1]))
        res = 0
        CurrMax = 0
        
        for a, d in properties:
            if d < CurrMax:
                res += 1
            CurrMax = max(CurrMax,d)
        return res