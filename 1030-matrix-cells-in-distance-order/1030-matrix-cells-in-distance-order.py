class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        
        output=[]
        for i in range(rows):
            for j in range(cols):
                output.append([i,j])
        return sorted(output, key = lambda p: abs(p[0] - rCenter) + abs(p[1] - cCenter))       
                
                
                
                
        