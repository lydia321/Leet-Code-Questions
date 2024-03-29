class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = []
        for i in nums:
            heap.append(-i)
        heapq.heapify(heap)

        Total_sum, count = -sum(heap), 0
        curr_sum, half_initial_sum= Total_sum, Total_sum/2
     
        for _ in range(len(nums)):  
            val = heapq.heappop(heap)
            curr = val/2
            # print(val,curr)
            heapq.heappush(heap,curr)
            count += 1
            curr_sum -= (abs(val) - abs(curr))
            # print(Total_sum,val,curr,curr_sum)
            expected_sum = Total_sum - curr_sum
            # print(Total_sum,expected_sum)
            if expected_sum >= half_initial_sum:
                break
        return count
            
            