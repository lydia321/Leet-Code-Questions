class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
                                                
        S1 = sorted(Counter(word1).values())                                
        S2 = sorted(Counter(word2).values())                               

        set1 = set(word1)                                           
        set2 = set(word2)                                           

        if S1 == S2 and set1 == set2:                      
            return True

        return False
