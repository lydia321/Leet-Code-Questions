class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:   
        graph = defaultdict(int)
        
        for i in trust:
            graph[i[0]] -= 1
            graph[i[1]] += 1
        print(graph)
        
        for i in range(1,n+1):
            if graph[i] == n - 1:
                return i
        return -1
        
        
        
        
         
        
        
        