class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if len(grid) == 1:
            return grid[0][0]
        #Theier are 4 possible moves for the 2 people,
        #1) Person 1 does down one row and  Person 2 does down one row
        #2) Person 1 does down one row and  Person 2 does right one col
        #3) Person 1 does down one col and  Person 2 does down one row
        #4) Person 1 does down one col and  Person 2 does right one col
        cache = {}
        out_of_bound = len(grid)
        
        def dfs(x0,x1,y0,y1):
            if (x0,x1,y0,y1) in cache:
                return cache[(x0,x1,y0,y1)]
            #if it goes out of bound
            if x1 >= out_of_bound or x0 >= out_of_bound or y0 >= out_of_bound or y1 >= out_of_bound:
                return -inf
            #if it hits a thorn 
            if grid[x0][x1] == -1 or grid[y0][y1] == -1:
                return -inf
            if x0 == y0 and x1 == y1:
                res = grid[x0][x1]
            else: 
                res = grid[x0][x1] + grid[y0][y1]
            
            if x0 == out_of_bound - 1 and x1 == out_of_bound - 1:
                return grid[x0][x1]
            if y0 == out_of_bound - 1 and y1 == out_of_bound - 1:
                return grid[y0][y1]
            
            res += max(dfs(x0+1,x1,y0 + 1,y1),
                      dfs(x0+1,x1,y0,y1 + 1),
                      dfs(x0,x1 + 1,y0 + 1,y1),
                      dfs(x0,x1 + 1,y0,y1 + 1))
            cache[(x0,x1,y0,y1)] = res
            
            return res
        
        final = dfs(0,0,0,0)
        if len(cache) == 0 or final < 0:
            return 0
        return final
        
        
            
