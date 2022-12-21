class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        res = []
        lookup = {}
        
        for i in range(len(nums)):
            lookup[nums[i]] = 1 + lookup.get(nums[i],0)
        
        for i in nums:
            adj1 = i - 1
            adj2 = i + 1
            
            if lookup[i] == 1 and adj1 not in lookup and adj2 not in lookup:
                res.append(i)
        return res