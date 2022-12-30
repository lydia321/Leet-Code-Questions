class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:    
        if len(nums) < 2 or k == 0:
            return 0
        nums.sort()
        l, r = 0, k - 1
        MinDiff = float('inf')
        while r < len(nums):
            MinDiff = min(MinDiff,nums[r]-nums[l])
            r += 1
            l += 1
        return MinDiff
    
    