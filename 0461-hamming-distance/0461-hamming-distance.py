class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        A = bin(x)[2:].zfill(50)
        B = bin(y)[2:].zfill(50)
        res = 0
        for i in range(50):
            if A[i] != B[i]:
                res += 1
        return res