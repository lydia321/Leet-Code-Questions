class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        #Bottom Up DP
        #Base Case 
        dp = [0,1]
        for i in range(n-2):
            dp.append(dp[-1] + dp[-2])
        return dp[-1] + dp[-2]    
    