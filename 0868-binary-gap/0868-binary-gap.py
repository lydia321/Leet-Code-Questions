class Solution:
    def binaryGap(self, n: int) -> int:
        val = bin(n)[2:]
        res = 0
        l = 0
        for r in range(len(val)):
            if val[r] == '1':
                res = max(res, r - l)
                l = r
        return res