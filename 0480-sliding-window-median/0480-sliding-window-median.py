from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        curr = SortedList()
        res = []
        idx = 0
        for i in range(len(nums)):
            curr.add(nums[i])
            
            #if len becomes greater than k
            if len(curr) > k:
                curr.remove(nums[idx])
                idx += 1
            
            if len(curr) == k:
                if len(curr)%2 == 0:
                    m1 = len(curr)//2
                    m2 = m1 - 1
                    res.append((curr[m1] + curr[m2])/2)
                else:
                    middle = len(curr)//2
                    res.append(curr[middle])
        return res
            
            