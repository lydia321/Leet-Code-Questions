class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        dp = [1]
        res.append(dp)
        
        for i in range(numRows - 1):
            curr_dp = []
            curr_dp.append(dp[0])
            if len(dp) > 1:
                for i in range(len(dp) - 1):
                    curr_dp.append(dp[i] + dp[i+1])
            curr_dp.append(dp[-1])
            
            dp = curr_dp
            res.append(dp)
        return res