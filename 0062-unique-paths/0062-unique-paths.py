class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        target_row = m - 1
        target_col = n - 1
        
        cache = {}

        def dp(row,col):
            if (row, col) in cache:
                return cache[(row,col)]
            if row == target_row and col == target_col :
                return 1
            elif row == m or col == n:
                return 0
            cache[(row,col)] = dp(row + 1,col) + dp(row,col + 1)
            return cache[(row,col)]
        
        return dp(0,0)
