class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen, prev, curr = set(), 0, 0
        for n in nums:
            prev, curr = curr, (curr + n) % k
            if curr in seen: return True
            seen.add(prev)
        return False
              
        
   