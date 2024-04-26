class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        formed = 0
        
        window = defaultdict(int)
        lookup = Counter(t)
        needed = len(lookup)
        l = 0
        res = ''
        curr_res_len = inf
        
        for r in range(len(s)):
            if s[r] in lookup:
                window[s[r]] += 1
                
                if window[s[r]] == lookup[s[r]]:
                    formed += 1
                
                while formed == needed:
                    curr_window_len = r - l + 1
                    if curr_window_len < curr_res_len:
                        curr_res_len = curr_window_len
                        res = s[l:r+1]
                        
                    if s[l] in window:
                        window[s[l]] -= 1
                        
                        if window[s[l]] < lookup[s[l]]:
                            formed -= 1
                    l += 1
        return res
        
        
        