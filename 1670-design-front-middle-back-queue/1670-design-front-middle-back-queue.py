class FrontMiddleBackQueue:

    def __init__(self):
        self.q = []
        self.counter = 0
        self.m = len(self.q)//2

    def pushFront(self, val: int) -> None:
        self.q.insert(0,val)
        self.counter += 1
       
    def pushMiddle(self, val: int) -> None:
        self.q.insert(len(self.q) // 2, val)
        self.counter += 1
        
    def pushBack(self, val: int) -> None:
        self.q.append(val)
        self.counter += 1
        
    def popFront(self) -> int:
        if self.counter == 0:
            return -1
        self.counter -= 1
        return self.q.pop(0)
        
    def popMiddle(self) -> int:
        if self.counter == 0:
            return -1
        self.counter -= 1
        return self.q.pop((len(self.q)-1)//2)
        
    def popBack(self) -> int:
        if self.counter == 0:
            return -1
        self.counter -= 1
        return self.q.pop()
        
        
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()