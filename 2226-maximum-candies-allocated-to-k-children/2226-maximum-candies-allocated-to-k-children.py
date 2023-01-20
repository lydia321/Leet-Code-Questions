class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 1
        r = max(candies)
      
        while l <= r:
            m = (l+r)//2
            res = 0
            for i in candies:
                res += (i//m)
            if res >= k:
                l = m + 1
            else:
                r = m - 1
        return r
            
      