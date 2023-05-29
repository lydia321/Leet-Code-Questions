from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.arr = []
        
    def book(self, start: int, end: int) -> bool:
        flag = True
        if len(self.arr) == 0:
            self.arr.append((start,end))
            return True
        for each in self.arr:
            if not flag: break
            if each[0] < end and each[1] > start:
                flag = False
        if flag:
            self.arr.append((start,end))
        return flag
                
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)