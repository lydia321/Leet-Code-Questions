class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=len(nums)//2
        nums.sort()
        return nums[m]
            
        