class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count = [0]* (n)
        used = [] #(end_time,room)
        available_rooms = [i for i in range(n)]
        meetings.sort()
        
        for start,end in meetings:
            #any finished meetings?
            while used and start >= used[0][0]:
                _ ,room = heapq.heappop(used)
                heapq.heappush(available_rooms,room)
                
            #are there no rooms available?
            if not available_rooms:
                end_time, room = heapq.heappop(used)
                end += (end_time - start)
                heapq.heappush(available_rooms,room)
            
            #add meeting and undate count
            room = heapq.heappop(available_rooms)
            heapq.heappush(used,[end,room])
            count[room] += 1
        print(count)
        return count.index(max(count))
            
        
        
        