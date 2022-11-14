class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = []
        self.counter = 0
        self.size= k
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.arr.insert(0,value)
            self.counter += 1
            return True
            
    
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.arr.append(value)
            self.counter += 1
            return True
    
    def deleteFront(self):
        if self.isEmpty():
            return False
        else:
            self.arr.pop(0)
            self.counter -= 1
            return True
    
    def deleteLast(self):
        if self.isEmpty():
            return False
        else:
            self.arr.pop()
            self.counter -= 1
            return True
        
    def getFront(self):
        if self.isEmpty():
            return -1
        else:
            return self.arr[0]
    
    def getRear(self):
        if self.isEmpty():
            return -1
        else:
            return self.arr[-1]   
    
    def isEmpty(self):
        if self.counter == 0:
            return True
        return False
    
    def isFull(self):
        if self.counter == self.size:
            return True
        return False
            
            
        
        
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()