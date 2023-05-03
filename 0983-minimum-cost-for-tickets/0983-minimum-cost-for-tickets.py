class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}
        def closest(i,num,days):
            key = days[i]
            while i < len(days) and key + num > days[i]:
                i+=1
            return i

        def dp(i):

            if i == len(days):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = min(dp(i+1)+costs[0], dp(closest(i,7,days))+costs[1], dp(closest(i,30,days))+costs[2])
            
            return cache[i]
        
        return dp(0)
