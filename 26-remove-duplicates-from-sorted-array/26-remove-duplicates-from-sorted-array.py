class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        l=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[l-1]:
                nums[l]=nums[i]
                l+=1
        return l        
        [1,1,2]
        [1,]
        