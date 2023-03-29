class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if -i not in res:
                res.append(-i)
        print(res)
        heapq.heapify(res)
        if len(res) < 3:
            return - heapq.heappop(res)
        
        idx = 3
        while idx > 0:
            heapq.heappop(res)
            idx -= 1
            if idx == 1:
                return -heapq.heappop(res)
       