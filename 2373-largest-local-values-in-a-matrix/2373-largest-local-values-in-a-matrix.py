class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid[0])
        res = [[0] * (n - 2)]* (n - 2)
        # print(res)
        
        for i in range(len(res)):
            curr_arr = []
            for j in range(len(res[i])):
                final = 0
                for rows in range(i, i + 3):
                    # print(grid[rows][j:j+3])
                    curr = max(grid[rows][j:j+3])
                    final = max(curr,final)
                # print(final)
                curr_arr.append(final)
            res[i] = curr_arr
        return res
                
                
            
        
        
        
        