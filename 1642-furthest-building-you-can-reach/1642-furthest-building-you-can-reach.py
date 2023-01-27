class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            curr_diff = heights[i+1] - heights[i]
            
            if curr_diff > 0:
                heapq.heappush(heap,curr_diff)
                
                #if we finish our ladders
                if len(heap) > ladders:
                    val = heapq.heappop(heap)
                    bricks -= val
                
                if bricks < 0:
                    return i
        return len(heights)-1