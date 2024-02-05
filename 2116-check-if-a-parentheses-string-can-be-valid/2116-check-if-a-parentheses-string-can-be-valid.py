class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        if len(s) % 2:  # Intuitively, odd-length s cannot be valid.
            return False
        valid = 0
        for i in range(len(s)):
            valid += 1 if s[i] == '(' or locked[i] == '0' else -1   
            if valid < 0:
                return False
        
        valid = 0
        for i in range(len(s) - 1, -1, -1):
            valid += 1 if s[i] == ')' or locked[i] == '0' else -1
            if valid < 0:
                return False

        return True
   
        
        