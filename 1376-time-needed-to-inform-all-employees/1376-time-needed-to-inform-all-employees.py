class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dict = defaultdict(list)
        headTime = 0
        for i in range(n):
            if manager[i] != -1:
                dict[manager[i]].append(i)
            else:
                headTime = informTime[i]
        # print(dict)
        
        queue = [[headID,0]]
        # print(queue)
        res = 0
        
        while queue:
         
            Id,time = queue.pop()
            res = max(time,res)
            
            if Id in dict:
                for each in dict[Id]:
                    queue.append((each,time + informTime[Id]))
            
        return res