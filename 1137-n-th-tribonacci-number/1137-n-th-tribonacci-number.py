class Solution:
    def tribonacci(self, n: int) -> int:
        #edge Case
        if n == 0:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        #base case
        dp = [0,1,1]
        
        for i in range(n-2):
            dp.append(dp[-1] + dp[-2] + dp[-3])
        return dp[-1]