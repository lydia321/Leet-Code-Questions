class Solution:
    def maxPower(self, s: str) -> int:
        l = res = 0
        r = count = 0
        
        while r < len(s):
            if s[l] == s[r]:
                count += 1
                res = max(res,count)
            else:
                l = r
                count = 1
            r += 1   
        return res