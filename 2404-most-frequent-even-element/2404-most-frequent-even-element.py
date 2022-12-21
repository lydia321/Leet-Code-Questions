class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hash = {}
        
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                hash[nums[i]] = 1 + hash.get(nums[i], 0)
        res = -1
        curr = 0
        for val,count in hash.items():
            if count > curr:
                res = val
                curr = count
            elif count == curr:
                res = min(res,val)
        return res
                