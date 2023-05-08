class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = 0
        r = len(mat) -1
        res = 0
        
        while len(mat) > 1:
            front = mat.pop(0)
            end = mat.pop()
            res += front[l] + front[r]
            res += end[l] + end[r]
            l += 1
            r -= 1

        if mat:
            mid = len(mat[0])//2
            res += mat[0][mid]
            
        return res