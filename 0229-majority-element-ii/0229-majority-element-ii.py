class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        apperance = len(nums)//3
        lookup = {}
        res = []
        
        for i in range(len(nums)):
            lookup[nums[i]] = 1 + lookup.get(nums[i], 0)
            if lookup[nums[i]] > apperance and nums[i] not in res:
                res.append(nums[i])
        return res