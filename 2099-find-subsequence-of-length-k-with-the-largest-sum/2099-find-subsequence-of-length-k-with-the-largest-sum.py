class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res = nums[:]
        heapq.heapify(nums)
        
        while (len(nums) > k):
            val = heapq.heappop(nums)
            res.remove(val)
        return res
                    
        