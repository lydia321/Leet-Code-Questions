class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        curr_dp = [i for i in triangle[-1]]  #Base Case
        
        for i in range(len(triangle)-2,-1,-1):
            next_dp = []
            for j in range(len(triangle[i])):
                next_dp.append(min ((triangle[i][j] + curr_dp[j]), (triangle[i][j] + curr_dp[j+1])))
            curr_dp = next_dp
        # print(curr_dp)
        return curr_dp[0]
                
     
        
        