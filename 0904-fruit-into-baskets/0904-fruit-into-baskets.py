class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = res = type = 0
        curr = {}
        
        for r in range(len(fruits)):
            curr[fruits[r]] = 1 + curr.get(fruits[r],0)
            while len(curr) > 2:
                curr[fruits[l]] -= 1
                
                if curr[fruits[l]] == 0:
                    del curr[fruits[l]]
                l += 1
            res = max(res,sum(curr.values()))
        return res
        