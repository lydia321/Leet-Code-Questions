class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            dict[i] = 1 + dict.get(i,0)
        print(dict)
        
        res = []
        heapq.heapify(res)
        
        for i in dict:
            heapq.heappush(res,(dict[i],i))
            if len(res) > k:
                heapq.heappop(res)   
        print(res)
        return [i[1] for i in res]
       