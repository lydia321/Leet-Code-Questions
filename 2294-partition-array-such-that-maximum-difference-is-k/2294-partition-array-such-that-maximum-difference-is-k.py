class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # same elements must be on the same subsequence
        # each sub[max - min] <= k
        # build minimum number of subsequences
        # return number of subsequences
        '''
        123456
        '''
        nums.sort()
        if nums[-1] - nums[0] <= k:
            return 1
        curr_min = nums[0]
        res = 1
        
        for curr_max in nums:
            if curr_max - curr_min > k:
                res += 1
                curr_min = curr_max
        return res
        