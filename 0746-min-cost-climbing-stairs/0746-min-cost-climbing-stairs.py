class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0,cost[-1]]
        
        for i in range(len(cost) - 2, -1, -1):
            dp.append(min(dp[-1] + cost[i],dp[-2] + cost[i]))
        # print(dp)
        return min(dp[-1],dp[-2])
        