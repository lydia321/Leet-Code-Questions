class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        lookup = {0:1}
        res = 0
        
        for r in range(len(nums)):
            curr += nums[r]
            value = curr - k
            if value in lookup:
                res += lookup[value]
            lookup[curr] = 1 + lookup.get(curr,0)
        return res
       
            
        
#         count = 0
#         curr = 0
        
#         for i in range(len(nums)): 
#             for j in range(i,len(nums)): 
                
#                 curr += nums[j]
#                 if curr == k:
#                     count += 1
#             curr = 0   
#         return count
                
        