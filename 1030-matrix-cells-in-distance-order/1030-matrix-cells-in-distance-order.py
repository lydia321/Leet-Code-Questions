class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        output=[]
        for i in range(rows):
            for j in range(cols):
                output.append([i,j])
        return sorted(output, key= lambda p: abs(p[0]-rCenter) + abs(p[1]- cCenter))        
        