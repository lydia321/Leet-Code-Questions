class Solution:
    def countPoints(self, rings: str) -> int:
        lookup = {}
        
        for i in range(1,len(rings),2):
            if rings[i] not in lookup.keys():
                lookup[rings[i]] = [rings[i-1]]
            else:
                lookup[rings[i]].append(rings[i-1])
        res = 0
    
        for rod,rings in lookup.items():
            curr = set(rings)
            if len(curr) == 3:
                res += 1
        return res
            
        