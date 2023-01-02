class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = {}
        for i in range(len(s)):
            if s[i] not in sMap :
                if t[i] in sMap.values():
                    return False
                sMap[s[i]] = t[i]
            else:
                if sMap[s[i]] != t[i]:
                    return False
        return True
    
  