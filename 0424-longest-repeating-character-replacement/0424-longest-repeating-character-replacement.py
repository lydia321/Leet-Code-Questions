class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        lookup = {}
        
        for r in range(len(s)):
            lookup[s[r]] = 1 + lookup.get(s[r], 0)
            
            while (r - l + 1) - max(lookup.values()) > k:
                lookup[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
        return res
            