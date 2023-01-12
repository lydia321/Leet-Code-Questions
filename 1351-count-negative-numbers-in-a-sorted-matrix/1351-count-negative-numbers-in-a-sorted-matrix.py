class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg_Count = 0
        
        for i in grid:
            l, r = 0, len(i)-1
            while l <= r:
                m = (l+r)//2                
                if i[m] < 0:
                    r = m - 1
                else:
                    l = m + 1
            neg_Count += len(i) - l 
                    
        return neg_Count
                