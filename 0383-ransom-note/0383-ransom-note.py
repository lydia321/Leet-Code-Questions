class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = sorted(magazine)
        
        for i in ransomNote:
            if i not in m:
                return False
            else:
                m.remove(i)
        return True    
            