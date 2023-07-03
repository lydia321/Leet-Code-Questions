class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        s = defaultdict(int)
        res = -inf
        for i in nums:
            curr = 0
            for each in str(i):
                curr += int(each)
            if curr not in s:
                s[curr] = i
            else:
                res = max(res,s[curr] + i)
                s[curr] = max(i,s[curr])
        return res if res != -inf else -1
            