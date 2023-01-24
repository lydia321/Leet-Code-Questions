class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        M = max(nums)
        
        for i in nums:
            if i != M and i*2 > M:
                return -1
        return nums.index(M)