class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        res = []
        l = 0
        pTable = {}
        sTable = {}
        
        for i in range(len(p)):
            pTable[p[i]] = 1 + pTable.get(p[i],0)
            sTable[s[i]] = 1 + sTable.get(s[i],0)
        
        if sTable == pTable: res.append(l)
        
        #sliding window
        for r in range(len(p),len(s)):
            sTable[s[r]] = 1 + sTable.get(s[r],0)
            sTable[s[l]] -= 1
            if sTable[s[l]] == 0:
                sTable.pop(s[l])
            l += 1
            if sTable == pTable:
                res.append(l)
        return res
            
            