class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        a = '01'*n
        b = '10'*n
        s = s + s
        
        a += a
        b += b
        flips_a = 0
        flips_b = 0
        l = 0
        res = inf
        for r in range(len(s)):
            if s[r] != a[r]:
                flips_a += 1
            if s[r] != b[r]:
                flips_b += 1
                
            if (r - l + 1) == n:
                
                res = min(res,flips_a,flips_b)
                
                if s[l] != a[l]:
                    flips_a -= 1
                if s[l] != b[l]:
                    flips_b -= 1
                l += 1
        return res
        
        
            
        
        