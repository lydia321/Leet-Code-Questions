class Solution:
    def Count_days(self, weights, mid):
        Count_Days = 1
        res = 0
        
        for i in weights:
            if (res + i) > mid:
                Count_Days += 1
                res = i
            else:
                res += i
        return Count_Days
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right)//2
            curr = self.Count_days(weights, mid)
            
            if curr > days:
                left = mid + 1
            else:
                right = mid
        return left
        