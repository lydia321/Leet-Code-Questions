class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        From = bin(start)[2:].zfill(100)
        To = bin(goal)[2:].zfill(100)
        res = 0
        for i in range(len(To)):
            if To[i] != From[i]:
                res += 1
        return res