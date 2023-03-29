class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heap.append(-i)
        print(heap)
        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            print(x,y)
            if x != y:
                diff = abs(y) - abs(x)
                heapq.heappush(heap,diff)
        
        if len(heap) == 0:
            return 0
        return abs(heap[0])
        