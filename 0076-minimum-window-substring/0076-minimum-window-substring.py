from collections import Counter, defaultdict
from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = Counter(t)
        min_len = inf
        res = ''
        window = {}
        l = 0
        required = len(lookup)
        formed = 0
        
        for r in range(len(s)):
            if s[r] in lookup:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == lookup[s[r]]:
                    formed += 1
                    
            while formed == required:
                window_size = r - l + 1
                if window_size < min_len:
                    min_len = window_size
                    res = s[l:r+1]
                    
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < lookup[s[l]]:
                        formed -= 1
                l += 1
        
        return res
