class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] in rows[i] or matrix[i][j] in cols[j]:
                    return False
                rows[i].add(matrix[i][j])
                cols[j].add(matrix[i][j])
        # print(rows,cols)
        return True