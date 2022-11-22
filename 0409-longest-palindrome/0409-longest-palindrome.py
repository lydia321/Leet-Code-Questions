class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = L = 0
        
        for i in Counter(s).values():
            if i%2 == 1:
                count += i-1 
                L += 1
            else:
                count += i
                       
        if L != 0: count += 1
            
        return count        
        
            
        
        