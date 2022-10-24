class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        MaxCount = 0
        for i in s:
            if i == '(' :
                count += 1
                MaxCount = max(MaxCount,count)
            elif i == ')' :
                count -= 1
                
        return MaxCount        