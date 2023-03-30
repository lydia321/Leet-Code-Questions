from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        curr = SortedList()
        l = 0
        res = []
        
        for r in range(len(nums)):
            curr.add(nums[r])
            
            if len(curr) > k:  #goes out of the window
                curr.remove(nums[l])
                l += 1
                
            
            if len(curr) == k:
                # if its even
                if len(curr)%2 == 0:
                    m1 = len(curr) // 2
                    m2 = m1 - 1
                    res.append((curr[m1] + curr[m2])/2)
                #if its odd
                else:
                    m = len(curr) // 2
                    res.append(curr[m])
        
        return res
            
            