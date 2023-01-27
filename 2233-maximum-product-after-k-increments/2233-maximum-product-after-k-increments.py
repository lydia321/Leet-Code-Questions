class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        modVal = (10**9) + 7
        heapq.heapify(nums)
        
        while k > 0:
            val = heapq.heappop(nums)
            heapq.heappush(nums,val + 1)
            k -= 1
        
        res = 1
        for i in nums:
            res = ((res%modVal)*(i%modVal)) % modVal
        return res % modVal
    
    