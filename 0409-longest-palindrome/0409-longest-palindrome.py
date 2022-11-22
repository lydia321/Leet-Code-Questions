class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        L = 0
        s.split(' ')
        S = Counter(s)
        
        for i in S.values():
            print(i)
            if i%2 == 1:
                i -= 1
                count += i
                L += 1
            else:
                count += i
                
           
                
        if L != 0:
            count += 1
        return count        
        
            
        
        