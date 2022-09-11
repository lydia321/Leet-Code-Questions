class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr=[]
        res = []
        
        for i, val in enumerate(points):
            output=(val[0]**2)+(val[1]**2)
            arr.append((output,i))
        arr.sort()
        arr=arr[:k]
        
        for j in arr:
            print(j)
            res.append(points[j[1]])
        
        return res
  