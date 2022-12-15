class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Table = {}
        s2Table = {}
        for i in range(len(s1)):
            s1Table[s1[i]] = 1 + s1Table.get(s1[i],0)
            s2Table[s2[i]] = 1 + s2Table.get(s2[i],0)
        
        l = 0
        if s1Table == s2Table: return True
        
        for r in range(len(s1),len(s2)):
            s2Table[s2[r]] = 1 + s2Table.get(s2[r],0)
            s2Table[s2[l]] -= 1
            
            if s2Table[s2[l]] == 0:     s2Table.pop(s2[l])
            l += 1
            if s1Table == s2Table: return True
        return False
        