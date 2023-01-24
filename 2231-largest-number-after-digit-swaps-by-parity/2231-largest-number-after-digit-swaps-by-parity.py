class Solution:
    def largestInteger(self, num: int) -> int:
        odd = []
        even = []
        for i in str(num):
            if int(i)%2 == 0:
                even.append(-int(i))
            else:
                odd.append(-int(i))
        heapq.heapify(odd)
        heapq.heapify(even)

        res = ''
        for i in str(num):
            if int(i)%2 == 0:
                res += str(abs(even[0]))
                heapq.heappop(even)
            else:
                res += str(abs(odd[0]))
                heapq.heappop(odd)
        return int(res)