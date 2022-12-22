class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        lookup = {}
        
        for i in range(len(s)):
            lookup[s[i]] = 1 + lookup.get(s[i],0)
        res = set()
        
        for i,count in lookup.items():
            res.add(count)
        return len(res) == 1
        