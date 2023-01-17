class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        a = min(nums)
        b = max(nums)
        res = 0
        
        for i in nums:
            if a < i < b:
                res += 1
            
        return res
        