class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque([(0,0,1)]) #r c l
        visited = set((0,0))
        directions = [[0,1],[1,0],[0,-1],[-1,0],
                     [1,1],[-1,-1],[1,-1],[-1,1]]
        while queue:
            r,c,l = queue.popleft()
            #IS it out of bound?
            if (min(r,c) < 0 or max(r,c) >= n or grid[r][c]):
                continue
            #Have we reached the bottom right cell?
            if (r == n - 1) and (c == n - 1):
                return l
            
            for dr,dc in directions:
                if (dr + r, dc + c) not in visited:
                    queue.append((dr + r, dc + c, l + 1))
                    visited.add((dr + r, dc + c))
        
        return -1
        