class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dict = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                dict[i+j].append(mat[i][j])
       
        res = []
        flag = True
        for i,val in dict.items():
            if flag:
                for each in range(len(val)-1,-1,-1):
                    res.append(val[each])
                flag = False
            else:
                for each in val:
                    res.append(each)
                flag = True
        return res
        