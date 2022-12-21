class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort() 
        l = res = total_window_sum = 0
        
        for r in range(len(nums)):
            total_window_sum += nums[r]
            largest_variable = nums[r]
            
            #invalid window
            while largest_variable * (r - l + 1) > total_window_sum + k:
                total_window_sum -= nums[l]
                l += 1
            
            res = max(res,r - l + 1)
        return res