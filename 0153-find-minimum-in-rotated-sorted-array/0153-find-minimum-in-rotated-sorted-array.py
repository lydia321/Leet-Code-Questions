class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[0]
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            m = (l+r)//2
            res = min(res,nums[l])
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m
        return res