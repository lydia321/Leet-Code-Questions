class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set(nums)
       
        if len(s) == len(nums):
             return False
        return True
#         h = set()
        
#         for i in nums:
#             if i in h:
#                 return True
#             h.add(i)
#         return False    
#         
        
        