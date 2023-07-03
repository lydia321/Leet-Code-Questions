class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set(nums)
     
        for i in range(len(nums)):
            val = str(nums[i])
            val = val[::-1]
            s.add(int(val))
        
        return len(s)
                
                