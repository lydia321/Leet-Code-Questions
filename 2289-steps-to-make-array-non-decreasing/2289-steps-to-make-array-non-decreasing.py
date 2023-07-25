class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        res = [0] * len(nums)
        stack = []
        for i in range(len(nums)):
            cur = 0
            while stack and nums[i] >= nums[stack[-1]]:
                cur = max(cur, res[stack.pop()])
            if stack:
                res[i] = cur + 1
            stack.append(i)
        return max(res)