class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output=[nums[0]]
        for i in range(1,len(nums)):
            nums[0]=nums[0]+nums[i]
            output.append(nums[0])    
        return output