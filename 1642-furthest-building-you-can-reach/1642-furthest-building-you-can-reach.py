class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = [] #differences where we will use ladder
        heapq.heapify(heap)
        curr_bricks = bricks
        for i in range(len(heights)-1):
            diff = heights[i] - heights[i+1]
            
            # if next height is bigger
            if diff < 0:
                heapq.heappush(heap,-diff)
                
                #if ladder is full
                if len(heap) > ladders:
                    val = heapq.heappop(heap)
                    curr_bricks -= val
                
                #if bricks is not enough
                if curr_bricks < 0:
                    return i
        
        return len(heights) - 1
        