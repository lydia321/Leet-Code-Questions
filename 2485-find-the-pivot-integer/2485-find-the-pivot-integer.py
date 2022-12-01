class Solution:
    def pivotInteger(self, n: int) -> int:
        res = []
        for i in range(1,n+1):
            res.append(i)
        
        l,r = 0, sum(res)
        
        for i in range(len(res)):
            l += res[i]
            
            if l == r:
                return i + 1
            else:
                r -= res[i]
        return -1
            