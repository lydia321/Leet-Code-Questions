class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        Map = {0:-1}
        curr = 0
        for i,n in enumerate(nums):
            curr += n
            r = curr%k
            if r not in Map:
                Map[r]=i
            elif i - Map[r] > 1:
                return True
        return False