class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        curr = []
        
        for i in s:
            # print(curr,res)
            if i in curr:
                res += 1
                curr = []
                curr.append(i)
            else:
                curr.append(i)
        if len(curr) > 0:
            res += 1
        return res