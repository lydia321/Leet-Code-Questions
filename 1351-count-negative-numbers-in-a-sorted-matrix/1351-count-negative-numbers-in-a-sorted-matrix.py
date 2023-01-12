class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg_Count = 0
        
        for i in grid:
            l, r = 0, len(i)-1
            while l <= r:
                m = (l+r)//2                
                if i[m] < 0:
                    neg_Count += r - m + 1
                    r = m - 1
                else:
                    l = m + 1         
        return neg_Count
                