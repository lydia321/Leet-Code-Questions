class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]
        
        for i in range(rowIndex):
            curr_dp = []
            curr_dp.append(dp[0])
            
            for i in range(len(dp) - 1):
                curr_dp.append(dp[i] + dp[i+1])          
            curr_dp.append(dp[-1])
            
            dp = curr_dp
        return dp