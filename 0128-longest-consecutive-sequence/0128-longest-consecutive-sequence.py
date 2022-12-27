class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        
        for i in nums:
            if i - 1 not in s:
                length_so_far = 1
                print(i)
                while i + length_so_far in s:
                    length_so_far += 1
                res = max(res,length_so_far)
        
        return res
                    