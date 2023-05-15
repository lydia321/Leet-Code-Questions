class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[] for i in range(len(s))]
        i = 0
        
        while i < len(s):   
            #go vertical
            for row in range(numRows):
                if i < len(s):
                    matrix[row].append(s[i])
                    i += 1  
            #go diagonal - up
            for row in range(numRows - 2,0,-1):
                if i < len(s):
                    matrix[row].append(s[i])
                    i += 1
                

        res = ''
        for row in matrix:
            for char in row:
                res += char
        return res