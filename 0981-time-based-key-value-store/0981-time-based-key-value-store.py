class TimeMap:

    def __init__(self):
        self.dict = {}    

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([value,timestamp])
    def get(self, key: str, timestamp: int) -> str:
        res = ''
        value = self.dict.get(key, [])
        r = len(value)-1
        l = 0
        
        while l <= r:
            m = (l+r)//2
            if value[m][1] == timestamp:
                return value[m][0]
            elif value[m][1] > timestamp:
                r = m - 1
            else:
                res = value[m][0]
                l = m + 1
                
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)