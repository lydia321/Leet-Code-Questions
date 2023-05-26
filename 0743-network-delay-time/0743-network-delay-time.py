class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dict,shortest_path = defaultdict(set),defaultdict(int)
        for i in times:
            dict[i[0]].add((i[1],i[2])) 
        for i in range(1,n):
            shortest_path[i] = -inf
        visited,res = set(),0
      
        queue = [(0,k)]
        
        while queue:
            curr = heapq.heappop(queue)
            if curr[1] not in visited:
                visited.add(curr[1])
                res = max(res,curr[0])
                nghs = dict[curr[1]]
                for ngh in nghs:
                    if ngh[0] not in visited:
                        heapq.heappush(queue,(ngh[1] + curr[0],ngh[0]))
        return res if len(visited) == n else -1
                        
            
            
            
        
        
        
        
        
                    
            
            
                