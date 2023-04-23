class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = [points[0]]
        
        for i in range(1,len(points)):
            if res[-1][1] >= points[i][0]:
                res[-1][1] = min(res[-1][1],points[i][1])
            else:
                res.append(points[i])
        return len(res)
                
        