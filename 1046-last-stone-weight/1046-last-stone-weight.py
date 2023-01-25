class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap,-i)
        print(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            
            if x != y:
                val = abs(y) - abs(x)
                heapq.heappush(heap,val)
        if len(heap) == 0:
            return 0
        return -heap[0]
                        