class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res
#         l = 0
#         r = len(nums)-1
        
#         while l <= r:
#             m = (l+r)//2
            
#             if nums[m] == target:
#                 res.append(m)
                
#             if nums[m] < target:
#                 l = m + 1
#             else:
#                 r = m - 1
        