class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.arr = []
        count = {}
        leader, m = -1, 0
        
        for i,person in enumerate(persons):
            count[person] = count.get(person, 0) + 1
           
            if count[person] >= m:
                m = count[person]
                leader = person
                
            self.arr.append((times[i], leader))
            
    def q(self, t: int) -> int:
        l = 0
        r = len(self.arr) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if self.arr[mid][0] == t: return self.arr[mid][1]
            
            if self.arr[mid][0] > t: r = mid - 1
            
            else: l = mid + 1
            
        return self.arr[r][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# def __init__(self, persons: List[int], times: List[int]):
       
