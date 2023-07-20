class SeatManager:

    def __init__(self, n: int):
        self.seat = [i for i in range(1,n+1)]
        # print(self.seat)
        heapq.heapify(self.seat)
        self.un = set()
    def reserve(self) -> int:
        curr = heapq.heappop(self.seat)
        self.un.add(curr)
        return curr
    
    def unreserve(self, seatNumber: int) -> None:
        self.un.remove(seatNumber)
        heapq.heappush(self.seat,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)