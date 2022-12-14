class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = 0
        curr = {}
        
        for r in range(len(s)):
            curr[s[r]] = 1 + curr.get(s[r],0)
            
            while (r - l + 1) - max(curr.values()) > k:
                curr[s[l]] -= 1
                l += 1
                
            res = max(res,r-l+1)
        return res