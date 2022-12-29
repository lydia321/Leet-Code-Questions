class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        Curr_Cost = 0
        l = 0
        res = 0
        
        for r in range(len(s)): 
            Curr_Cost += abs(ord(s[r])-ord(t[r]))
            
            while Curr_Cost > maxCost:
                Curr_Cost -= abs(ord(s[l])-ord(t[l]))
                l += 1
            res = max(res, r - l + 1)
        return res
            