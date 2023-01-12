class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.Binarysearch(nums, target, True)
        right = self.Binarysearch(nums, target, False)
        return [left,right]
    def Binarysearch(self,nums,target,leftbias):
        l , r = 0 , len(nums)-1
        x = -1
        while l <= r:
            m = (l+r)//2
            
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                x = m
                if leftbias:
                    r = m - 1
                else:
                    l = m + 1
        return x
    
    