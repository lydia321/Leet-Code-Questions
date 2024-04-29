class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        deque = collections.deque()
        for r in range(len(nums)):
            while deque and nums[deque[-1]] <= nums[r]:
                    deque.pop()
            deque.append(r)
            if l > deque[0]:
                deque.popleft()
            if (r + 1) >= k:
                res.append(nums[deque[0]])
                l  += 1
        return res
            
            
            
            
        