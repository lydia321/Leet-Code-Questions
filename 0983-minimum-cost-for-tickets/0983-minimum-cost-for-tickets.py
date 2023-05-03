class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}
        
        def closest(i,num):
            key = days[i]
            while i < len(days) and key + num > days[i]:
                i+=1
            return i

        def dp(i):

            if i == len(days):
                return 0
            if i in cache:
                return cache[i]
            #First choice : add the first cost and go to next index
            choice1 = dp(i+1) + costs[0]
            #second choice: add second cost and go to index larger index from days[i] + 7
            choice2 = dp(closest(i,7)) + costs[1]
            #third choice: add third cost and go to index larger index from days[i] + 30
            choice3 = dp(closest(i,30)) + costs[2]
            
            cache[i] = min(choice1,choice2,choice3)   
            return cache[i]
        
        return dp(0)
