class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = defaultdict(list)
        heap = []
        for i in arr:
            val = abs(x - i)
            if val not in heap :heapq.heappush(heap,val)
            diff[val].append(i)
        # print(diff,heap)
        res = []
        while len(res) < k:
            curr = heapq.heappop(heap)
            for i in diff[curr]:
                if len(res) < k: res.append(i)
        res.sort()
        return res
                    
            
        
        
            