class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a,b) for a,b in zip(nums1,nums2)]
        pairs.sort(key = lambda x: -x[1])
        min_heap = []
        n1Sum,res = 0,0
        
        for n1,n2 in pairs:
            n1Sum += n1
            heapq.heappush(min_heap,n1)
            
            if len(min_heap) > k:
                n1Pop = heapq.heappop(min_heap)
                n1Sum -= n1Pop
            if len(min_heap) == k:
                res = max(res,n1Sum*n2)
        return res
