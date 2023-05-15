class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = []
        for _ in range(numRows):
            matrix.append([])
        diagonal = False
        i = 0
        while i < len(s):
            if not diagonal:
                for row in matrix:
                    if i < len(s):
                        row.append(s[i])
                        i += 1
                diagonal = True
            if diagonal:
                for row in range(numRows - 2, 0, -1):
                    if i < len(s):
                        matrix[row].append(s[i])
                        i += 1
                diagonal = False
        # print(matrix)
        res = ''
        for rows in matrix:
            for char in rows:
                res += char
        return res