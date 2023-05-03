class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}
        def closest(i,days,arr):
            key = arr[i]
            while i<len(arr) and arr[i]< key+days:
                i+=1
            return i

        def dp(days,i):

            if i>=len(days):
                return 0
            if days[i] in cache:
                return cache[days[i]]
            
            cache[days[i]] = min(dp(days,closest(i,1,days))+costs[0], dp(days,closest(i,7,days))+costs[1], dp(days,closest(i,30,days))+costs[2])
            
            return cache[days[i]]
        
        return dp(days,0)
