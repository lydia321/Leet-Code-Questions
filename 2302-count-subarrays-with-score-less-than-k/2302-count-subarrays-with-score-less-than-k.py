class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = l = curr = 0

        for r in range(len(nums)):
            curr += nums[r]
                     
            while curr*(r - l + 1) >= k:
                curr -= nums[l]
                l += 1
            count +=  r - l + 1
            
        return count
                
            
            
        
       