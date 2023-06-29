class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        curr = set()
        curr_sum = 0
        l = 0
        
        for r in range(len(nums)):
            # print(curr)
            if nums[r] not in curr:
                curr.add(nums[r])
                curr_sum += nums[r]
            else:
                res = max(res,curr_sum)
                while curr and nums[r] in curr:
                    curr.remove(nums[l])
                    curr_sum -= nums[l]
                    l += 1
                curr.add(nums[r])
                curr_sum += nums[r]
        res = max(res,curr_sum)
        return res
                
        
      