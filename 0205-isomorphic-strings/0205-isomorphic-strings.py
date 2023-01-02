class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for i in range(len(s)):
            if s[i] not in sMap and t[i] not in tMap :
                sMap[s[i]] = t[i]
                tMap[t[i]] = s[i]
            elif s[i] in sMap :
                if sMap[s[i]] != t[i]:
                    return False
            elif t[i] in tMap:
                if tMap[t[i]] != s[i]:
                    return False
        return True
    
  