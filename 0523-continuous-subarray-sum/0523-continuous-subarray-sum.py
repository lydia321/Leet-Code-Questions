class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        lookup = {0:-1}
        curr = 0
        
        for i in range(len(nums)):
            curr += nums[i]
            reminder = curr%k
            if reminder in lookup:
                if i - lookup[reminder] > 1:
                    return True
            else:
                lookup[reminder] = i
        return False    
            