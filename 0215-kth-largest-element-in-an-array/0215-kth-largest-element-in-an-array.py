class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = nums
        heapq.heapify(res)
        
        while len(res) > k:
            heapq.heappop(res)
        return res[0]
        
        