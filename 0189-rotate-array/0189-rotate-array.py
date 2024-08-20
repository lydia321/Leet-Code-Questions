class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > len(nums):
            k -= len(nums)
        b = nums[:len(nums) - k]
        a = nums[len(nums) - k:]
        a.extend(b)
        for i in range(len(nums)):
            nums[i] = a[i]
        
        
        