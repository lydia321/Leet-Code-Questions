class Solution:
    def reorganizeString(self, s: str) -> str:
        dict = defaultdict(int)
        for i in s:
            dict[i] += 1
        heap = []
        heapq.heapify(heap)
        for i in dict:
            heapq.heappush(heap,(-dict[i],i))
        
        res = ''
        while heap:
            cnt,c = heapq.heappop(heap) 
            if not res or c != res[-1]:
                print(res)
                res += c
                cnt *= -1
                cnt -= 1
                if cnt > 0:
                    heapq.heappush(heap,(-cnt,c))
            else:
                if not heap: return ''
                cnt2,c2 = heapq.heappop(heap)
                res += c2
                cnt2 *= -1
                cnt2 -= 1
                if cnt2 > 0:
                    heapq.heappush(heap,(-cnt2,c2))
                
                heapq.heappush(heap,(cnt,c)) 
        return res
            
            