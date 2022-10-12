class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        output = []
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                output.append(nums[i])
              
        return output
        
        