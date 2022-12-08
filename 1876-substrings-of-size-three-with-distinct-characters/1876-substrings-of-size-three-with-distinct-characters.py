class Solution:
    def countGoodSubstrings(self, nums: str) -> int:
        l = count = 0
        m = 1
        
        for r in range(2,len(nums)):
            if nums[l] != nums[m] and nums[m] != nums[r] and nums[l] != nums[r]:
                count += 1
            l += 1
            m += 1
        return count
            
            
        