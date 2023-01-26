class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        List = []
        for i in nums:
            List.append(-i)
        heapq.heapify(List)
        print(List)
        
        res = 0
        for _ in range(k):
            val = heapq.heappop(List)
            res = val
        return -res
            