class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = [-1]
        
        for i in nums:
            if i > heap[0]:
                if len(heap) == 2:
                    heapq.heappop(heap)
                heapq.heappush(heap,i)
        
            
        res = (heap[0] - 1) * (heap[1] - 1)
        return res