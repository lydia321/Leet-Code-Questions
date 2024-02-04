class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}
        def dfs(i):
            if i == len(arr):
                return 0
            if i in cache:
                return cache[i]
            res = 0
            curr_max = 0
            for j in range(i, min(len(arr),i + k)):
                curr_max = max(curr_max,arr[j])
                res = max(res, dfs(j + 1) + curr_max * (j - i + 1))
            cache[i] = res
            return cache[i]
        return dfs(0)
        