class UndergroundSystem:

    def __init__(self):
        self.system = defaultdict(list)
        self.pending = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.pending[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        currstation,start = self.pending.pop(id)
        time = t - start
        self.system[(stationName,currstation)].append(time)
        # print(self.system)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        timelist = self.system[(endStation,startStation)]
        # print(startStation,endStation)
        # print(self.system[(str(startStation),str(endStation))])
        l = len(timelist)
        res = sum(timelist)/l
        return res
            
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)