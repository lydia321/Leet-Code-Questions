class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Bottom Up DP
        #[25,15,20,0]
        #[6,105,5,5,4,102,3,2,100,1,0]
        #Every idx will choose optimally from the two optimal solutions infront of it
        
        #Base case 
        dp = [0,cost[-1]]
        
        for i in range(len(cost) - 2, -1, -1):
            dp.append(min(dp[-1] + cost[i],dp[-2] + cost[i]))
        #Finally is it optimal to skip the first step or not
        return min(dp[-1],dp[-2])
        