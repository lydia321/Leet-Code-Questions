class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        res = []
        curr = -1
        idx = -1
        for i in range(len(mat)):
            if curr < max(mat[i]):
                curr = max(mat[i])
                idx = i
        res.append(idx)
        res.append(mat[idx].index(curr))
        return res
            
                
                