class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
         stones = [-s  for s in stones]
         heapq.heapify(stones)
        
         while len(stones) > 1:
                
            # remove two stones
             a = heapq.heappop(stones)
             b = heapq.heappop(stones)
             if a != b:
                    
                 diff = abs(a)-abs(b)
                 heapq.heappush(stones, -diff)
            
         if len(stones) == 0:
             return 0
         return abs(stones[0])
    