class RangeModule:

    def __init__(self):
        self.tracks = []
        
        #If idx is even, it is not included in the range
        #If idx is odd, it is included in the range
    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.tracks, left)
        end = bisect.bisect_right(self.tracks,right)
        
        subtrack = []
        if start%2 == 0:
            subtrack.append(left)
        if end%2 == 0:
            subtrack.append(right)
        self.tracks[start:end] = subtrack
        
    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.tracks,left)
        end = bisect.bisect_left(self.tracks, right)
        # print(self.tracks,start,end)
        return start == end and start%2 == 1
        

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.tracks,left)
        end = bisect.bisect_right(self.tracks, right)
        
        # print(self.tracks)
        subtrack = []
        if start%2 == 1:
            subtrack.append(left)
        if end%2 == 1:
            subtrack.append(right)
        self.tracks[start:end] = subtrack
        # print(self.tracks)
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)