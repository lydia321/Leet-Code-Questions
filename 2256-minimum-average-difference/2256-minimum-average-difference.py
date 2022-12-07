class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        ans = float("inf")
        total = sum(nums)
        l = len(nums)
        idx = prefix_sum = 0
        
        for i in range(len(nums)):
            total -= nums[i]
            prefix_sum += nums[i]
            l -= 1
            a = prefix_sum//(i+1)
            
            if l != 0: b = total//l
            else: b = 0
            
            res = abs(a-b)
            if res < ans:
                ans = res
                idx = i
        return idx   
            
        