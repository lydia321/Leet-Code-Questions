class Solution:
    def findScore(self, nums: List[int]) -> int:
        res = 0
        l = []
        for i in range(len(nums)):
            l.append((nums[i],i))
        l.sort()
        count = len(nums)
        visited = set()
        while count > 0:
            curr,i = l.pop(0)
            # print(nums,curr)
            if i not in visited:
                res += curr
                visited.add(i)
                count -= 1
                if i > 0 and i - 1 not in visited:
                    count -= 1
                    visited.add(i - 1)
                    nums[i - 1] *= -1
                if i < len(nums) - 1 and i + 1 not in visited:
                    visited.add(i + 1)
                    count -= 1
             
        return res
            