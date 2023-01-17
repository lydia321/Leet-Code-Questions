class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        S = sorted(set(arr))
        dict = {}
        res = []
    
        for i,val in enumerate(S):
            dict[val] = i + 1
              
        print(dict)
        
        for i in arr:
            res.append(dict[i])
        return res
    
    