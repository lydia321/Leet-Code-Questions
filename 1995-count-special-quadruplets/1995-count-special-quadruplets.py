class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        pac, atl = set(), set()
        def dfs(r,c,prev,visited):
            if (r,c) in visited or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prev:
                return 
            visited.add((r,c))
            dfs(r + 1,c,heights[r][c],visited)
            dfs(r - 1, c,heights[r][c],visited)
            dfs(r, c + 1, heights[r][c],visited)
            dfs(r,c - 1, heights[r][c],visited)
 
        for c in range(cols):
            dfs(0,c, heights[0][c],pac)
            dfs(rows - 1,c,heights[rows - 1][c],atl)
        for r in range(rows):
            dfs(r,0,heights[r][0],pac)
            dfs(r,cols - 1,heights[r][cols - 1],atl)
        #Atlantic 
       
        res = []
        for p in pac:
            if p in atl:
                res.append(p)
        return res
        
        