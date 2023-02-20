class Solution:
    def findPairs(self, nums: List[int], k: int) -> int: 
        
        if k == 0:
            count = 0
            dict = Counter(nums)
            for key,val in dict.items():
                if val > 1:
                    count += 1
            return count
        
        nums = list(set(nums))
        nums.sort()
        count = 0
        l, r = 0 ,1
        while r < len(nums):
            curr = nums[r] - nums[l]
            if curr == k:
                count += 1
            if curr > k:
                 l += 1
            else:
                r += 1
        return count
       
        