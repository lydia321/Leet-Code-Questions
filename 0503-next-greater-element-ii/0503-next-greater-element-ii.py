class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        res = [-1]*n
        stack = []
        nums *= 2
        for i in range(n*2):
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[i]
            if i < n:
                stack.append(i)
        return res
                
            
        