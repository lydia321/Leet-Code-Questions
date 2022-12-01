class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        lenght = float("inf")
        curr = 0
        
        for r in range( len(nums)):
            curr += nums[r]
            while curr >= target: 
                curr -= nums[l]
                lenght = min(lenght, (r-l+1))
                l += 1
                
        return 0 if lenght == float("inf") else lenght
      