class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0
        
        for _ in range(len(grid[0])):
            FinalMax = 0
            
            for i in grid:
                CRM = max(i)
                FinalMax = max(FinalMax,CRM)
                i.remove(CRM)
            res += FinalMax
     
        return res
        
        