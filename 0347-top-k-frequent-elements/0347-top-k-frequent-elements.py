class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            dict[i] = 1 + dict.get(i,0)
        print(dict)
        
        heap = []
        for i in dict:
            heapq.heappush(heap,(-dict[i],i))
        print(heap)
        
        res = []
        for i in range(k):
            val = heapq.heappop(heap)
            res.append(val[1])
        return res
            
