from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.arr = SortedList()

    def addNum(self, num: int) -> None:
        self.arr.add(num)

    def findMedian(self) -> float:
        l = len(self.arr)
        if l%2 == 0:
            middle1 = l // 2
            middle2 = middle1 - 1
            return (self.arr[middle1] + self.arr[middle2] ) / 2
        else:
            middle = l // 2
            return self.arr[middle]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()