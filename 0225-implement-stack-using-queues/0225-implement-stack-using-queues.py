class MyStack:

    def __init__(self):
        self.arr = collections.deque()
        

    def push(self, x: int) -> None:
        self.arr.append(x)
        
        for _ in range(len(self.arr)-1):
            self.arr.append(self.arr.popleft())

    def pop(self) -> int:
        return self.arr.popleft()
        
    def top(self) -> int:
        return self.arr[0]

    def empty(self) -> bool:
        return len(self.arr) == 0
            


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

   