class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        lookup = set()
        res = set()
        
        for i in range(len(s)-9):
            curr = s[i:i+10]
            if curr in lookup:
                res.add(curr)
            lookup.add(curr)     
        return res
        