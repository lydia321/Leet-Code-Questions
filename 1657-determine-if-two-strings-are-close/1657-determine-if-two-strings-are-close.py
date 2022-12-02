class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        s1 = set(word1)
        s2 = set(word2)
        
        C1 = sorted(Counter(word1).values())
        C2 = sorted(Counter(word2).values())
        
        if s1 == s2 and C1 == C2:
            return True
        return False
    
        