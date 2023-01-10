class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_sum,max_sum = float('-inf'),float('-inf')
        for n in nums:
            curr_sum += n
            curr_sum = max(curr_sum,n)
            max_sum = max(max_sum,curr_sum)
      
        left_sum = [0]*len(nums)
        left_max = [0]*len(nums)
        right_sum = [0]*len(nums)
        
        curr = 0
        for i in range(len(nums)-1,-1,-1):
            curr += nums[i]
            left_sum[i] = curr
        
        left_max_curr = float('-inf')
        for i in range(len(nums)-1,-1,-1):
            left_max_curr = max(left_max_curr,left_sum[i])
            left_max[i] = left_max_curr
        
        rcurr = 0
        for i in range(len(nums)):
            rcurr += nums[i]
            right_sum[i] = rcurr
        
        Max_sum,curr_max = float('-inf'),float('-inf')
        for i in range(len(nums)-1):
            curr_max = left_max[i+1] + right_sum[i]
            Max_sum = max(Max_sum,curr_max)
        
        return max(Max_sum,max_sum)