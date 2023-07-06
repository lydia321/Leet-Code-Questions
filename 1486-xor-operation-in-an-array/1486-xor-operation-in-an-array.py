class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = []
        for i in range(n):
            arr.append(start + (2 * i))
        # print(arr)
        res = 0
        for i in arr:
            res ^= i
        return res