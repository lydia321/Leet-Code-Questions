class MinStack:

    def __init__(self):
        self.arr = []
        self.m = []
    def push(self, val: int) -> None:
        self.arr.append(val)
        
        if self.m:
            self.m.append(min(val,self.m[-1]))
        else:
            self.m.append(val)
    def pop(self) -> None:
        self.arr.pop()
        self.m.pop()
    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.m[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()