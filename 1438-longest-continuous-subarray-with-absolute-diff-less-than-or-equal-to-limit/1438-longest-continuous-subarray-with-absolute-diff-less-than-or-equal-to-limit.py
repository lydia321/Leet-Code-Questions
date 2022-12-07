class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from sortedcontainers import SortedList
        
        sorted_list = SortedList()
        l, max_length = 0, 0
        for r in range(len(nums)):
            # move r
            sorted_list.add(nums[r])
           
            while sorted_list[-1] - sorted_list[0] > limit:
                # move l
                sorted_list.remove(nums[l])
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length
        