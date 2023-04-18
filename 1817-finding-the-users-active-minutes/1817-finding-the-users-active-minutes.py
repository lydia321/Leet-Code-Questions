class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dict = defaultdict(list)
        
        for i in logs:
            dict[i[0]].append(i[1])
        
        res = [0 for i in range(k)]
        
        for i,val in dict.items():
            res[len(set(val)) - 1] += 1
        return res