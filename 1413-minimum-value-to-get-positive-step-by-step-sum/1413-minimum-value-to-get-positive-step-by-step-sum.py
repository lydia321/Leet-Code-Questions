class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        arr = [nums[0]]
        
        for i in range(1,len(nums)):
            arr.append(arr[-1]+nums[i])
        
        print(arr)
        res = min(arr)
        if res < 0:
            res = abs(res)+1
            return res
        else: return 1
        
        