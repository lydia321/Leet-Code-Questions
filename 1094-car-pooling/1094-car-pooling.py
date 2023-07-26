class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1]) 
        heap = []
        curr = 0
        
        for each in  trips: 
            #time comes
            while heap and heap[0][0] <= each[1]:
                val = heapq.heappop(heap)
                curr -= val[1]
            
            curr += each[0]
            heapq.heappush(heap,(each[2],each[0]))
            if curr > capacity:
                return False
            
        return True