class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        Total = sum(nums)
        curr = 0
        heap = []
        for i in nums:
            heapq.heappush(heap,-i)
        res = []
        
        while Total >= curr:
            
            val = heapq.heappop(heap)
            res.append(abs(val))
            curr += abs(val)
            Total -= abs(val)
            # print(Total,curr,res)
        return res