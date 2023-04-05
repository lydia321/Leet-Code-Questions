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
        
#         #Top Down DP
#         def dp(n,visited):
#             if n in visited:
#                 return visited[n]
#             else:
#                 visited[n] = dp(n-1,visited) + dp(n-2,visited)
#             return visited[n]
            
#         return dp(n,{0:0,1:1})
        