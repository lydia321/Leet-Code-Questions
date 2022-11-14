class MyCircularQueue:

    def __init__(self, k: int):
        self.stack = []
        self.counter = 0
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.stack.append(value)
        self.counter += 1
        return True
    

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.stack.pop(0)
        self.counter -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.stack[0]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.stack[-1]
        

    def isEmpty(self) -> bool:
        if self.counter == 0:
            return True
        return False
        
    def isFull(self) -> bool:
        if self.counter==self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()