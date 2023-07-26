class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour):
            return -1

        def isEnoughSpeed(s):
            curr = 0
            for i in range(len(dist)):
                if i != len(dist) - 1:
                    curr += ceil(dist[i]/s)
                else:
                    curr += dist[i]/s
                
            return curr <= hour

        l, r= 1, 10**7
        
        while l < r:
            speed = (l+r)//2
            if isEnoughSpeed(speed):
                r = speed
            else:
                l = speed + 1
        
        return l
        
      