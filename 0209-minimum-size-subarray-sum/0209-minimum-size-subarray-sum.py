class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        lenght = float("inf")
        curr = nums[0]
        while r < len(nums) and l <= r:
            if curr < target:
                r += 1
                if r < len(nums): curr += nums[r]
            else:
                lenght = min(lenght, r-l+1)
                curr -= nums[l]
                l += 1
                
        return 0 if lenght == float("inf") else lenght
       
        