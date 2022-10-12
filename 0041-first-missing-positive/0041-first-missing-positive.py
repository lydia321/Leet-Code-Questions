class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lookup = set(nums)
        count = 1
        
        while count in lookup:
            count+=1
        return count
                
        