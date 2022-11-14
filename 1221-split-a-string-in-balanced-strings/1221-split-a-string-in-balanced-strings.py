class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = r = 0
        count = 1
        
        for i in range(len(s)):
            if s[i] == 'R':
                r += 1 
              
            else:
                l += 1
            
            if l == r:
                if l+r == len(s):
                    return count
                else:
                    l = 0
                    r = 0
                    count += 1
                
        return count-1        
           
        
        