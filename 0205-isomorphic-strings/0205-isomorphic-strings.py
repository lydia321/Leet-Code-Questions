class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}
        
        for a,b in zip(s,t):
            if a not in s1 and b not in s2:
                s1[a] = b
                s2[b] = a
            elif s1.get(a) != b :
                return False
        return True    
       
      
                
        