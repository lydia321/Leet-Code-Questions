class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr = 0
        
        for i in range(len(nums)):
            if curr in nums:
                curr += 1
                
        return curr