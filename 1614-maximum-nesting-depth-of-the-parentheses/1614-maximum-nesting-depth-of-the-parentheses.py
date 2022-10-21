class Solution:
    def maxDepth(self, s: str) -> int:
        res = curr = 0
        
        for i in s:
            if i == "(" :
                curr += 1
                res = max(curr,res)
            elif i == ")":
                curr -= 1
            
        return res      
                