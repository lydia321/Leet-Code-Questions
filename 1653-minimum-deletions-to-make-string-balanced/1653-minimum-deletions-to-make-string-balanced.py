class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_a = 0
        count_b = 0
        a = [0]*len(s)
        b = [0]*len(s)
        for i in range(len(s)):
            a[i] = count_b
            if s[i] == 'b':
                count_b += 1
        for i in range(len(s)- 1, -1, -1):
            b[i] = count_a
            if s[i] == 'a':
                count_a += 1
        res = inf
        for m in range(len(s)):
            res = min(res, a[m] + b[m])
        return res
        