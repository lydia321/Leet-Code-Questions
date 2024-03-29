class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        flag = False
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                if flag: 
                    return False
                if i > 1 and nums[i] <= nums[i-2]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
                flag = True

        return True   