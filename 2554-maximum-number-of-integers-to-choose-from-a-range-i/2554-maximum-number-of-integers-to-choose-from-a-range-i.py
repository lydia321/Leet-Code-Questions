class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s = set(banned)
        for i in banned:
            if i < n: s.add(i)
            else: break     
        # print(s)
        res = 0
        curr_sum = 0
        for i in range(1,n + 1):
            # print(i)
            if (i + curr_sum) > maxSum:
                return res
            if i not in s:
                curr_sum += i
                res += 1
        return res
        
        