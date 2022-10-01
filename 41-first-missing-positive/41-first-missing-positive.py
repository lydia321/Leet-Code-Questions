class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = set(nums)
        count = 1
        while count in n:
            count+=1
        return count
        
           