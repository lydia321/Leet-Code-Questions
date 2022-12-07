class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       
        ps = {0:1}
        res = 0
        curr = 0
        
        for i in nums:
            curr += i
            if (curr - k) in ps:
                res += ps[curr-k]
            if curr not in ps:
                ps[curr] = 1
            else:
                ps[curr] += 1
                
            
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
                
        