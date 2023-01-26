class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        nums = []
        for i in piles:
            nums.append(-i)
        heapq.heapify(nums)
        
        for _ in range(k):
            val = -heapq.heappop(nums)
            a = val//2
            # print(val,a)
            heapq.heappush(nums,-(val - a))
        
        return -sum(nums)
        