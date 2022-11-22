class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        lookup = set(nums)
        
        for i in nums:
            p = diff+i
            n = i-diff
            
            if p in lookup and n in lookup:
                res += 1
        return res       
        
        