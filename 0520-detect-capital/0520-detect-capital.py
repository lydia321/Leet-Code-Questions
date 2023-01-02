class Solution:
    def AllCaptial(self, word):
        for i in word:
             if i.islower():
                return False
        return True
    
    def AllLower(self, word):
        for i in word:
            if i.isupper():
                return False
        return True
    
    def FirstCaptial(self, word):
        if word[0].islower():
             return False
        
        for i in range(1, len(word)):
            if word[i].isupper():
                return False
        return True
        
    def detectCapitalUse(self, word: str) -> bool:
        return self.AllCaptial(word) or self.AllLower(word) or self.FirstCaptial(word)
