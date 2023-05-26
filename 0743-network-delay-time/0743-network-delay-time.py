class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dict,visited = defaultdict(set),set()
        for i in times:
            dict[i[0]].add((i[1],i[2]))
        #Dijkstra's Algorithm
        res = 0
        queue = [(0,k)]
        
        while queue:
            cost,node = heapq.heappop(queue)
            
            if node not in visited:
                visited.add(node)
                res = max(res,cost)
                for each in dict[node]:
                    if each[0] not in visited:
                        heapq.heappush(queue,(cost + each[1],each[0]))
                        
        return res if len(visited) == n else -1
            
            
            
        
        
        
        
        
                    
            
            
                