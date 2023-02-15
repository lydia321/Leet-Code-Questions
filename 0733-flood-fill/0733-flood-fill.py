class Solution:
   
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue, visted,row,col,wanted_color = [],set(),len(image),len(image[0]),image[sr][sc]
        image[sr][sc] = color
        queue.append([sr,sc])
        visted.add((sr,sc))
        while queue:
            # print(queue,visted)
            for _ in range(len(queue)):
                r,c = queue.pop(0)
                if 0 <= c+1 < col and image[r][c+1] == wanted_color and (r,c+1) not in visted :
                    visted.add((r,c+1))
                    queue.append([r,c+1])
                    image[r][c+1] = color
                
                if 0 <= c-1 < col and image[r][c-1] == wanted_color and (r,c-1) not in visted:
                    visted.add((r,c-1))
                    queue.append([r,c-1])
                    image[r][c-1] = color
                
                if 0 <= r+1 < row and image[r+1][c] == wanted_color and (r+1,c) not in visted:
                    visted.add((r+1,c))
                    queue.append([r+1,c])
                    image[r+1][c] = color
                
                if 0 <= r-1 < row and image[r-1][c] == wanted_color and (r-1,c) not in visted:
                    visted.add((r-1,c))
                    queue.append([r-1,c])
                    image[r-1][c] = color
        return image