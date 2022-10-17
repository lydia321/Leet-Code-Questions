class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        result = set(sentence)
        if len(result) == 26:
            return True
        return False
        
            
        