class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        count = 0
        
        for r in range(2,len(s)):
            m = l+1
            if s[l] != s[m] and s[l] != s[r] and s[r] != s[m]:
                count += 1
            l += 1
        return count
            
            
        