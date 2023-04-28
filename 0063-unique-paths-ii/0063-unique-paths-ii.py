class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        obs = []
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    obs.append((i,j))
        
        target_row = len(obstacleGrid) - 1
        target_col = len(obstacleGrid[0]) - 1
        
        cache = {}
        
        def dp(row,col):
            if (row,col) in cache:
                return cache[(row,col)]
            if (row,col) in obs or (row == target_row + 1) or (col == target_col + 1):
                return 0
            elif target_row == row and target_col == col:
                return 1
                        
            cache[(row,col)] = dp(row + 1,col) + dp(row,col + 1)
            return cache[(row,col)]
        
        return dp(0,0)