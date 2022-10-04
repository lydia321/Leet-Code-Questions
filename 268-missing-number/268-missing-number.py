class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=set(nums)
        count=0
        while count in nums:
            count+=1
        return count    