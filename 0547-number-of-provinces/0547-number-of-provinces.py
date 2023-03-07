class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j]:
                    graph[i+1].append(j+1)
                    graph[j+1].append(i+1)
        print(graph)
        visited = set()
        res = 0
        def dfs(city):
            visited.add(city)
            for i in graph[city]:
                if i not in visited:
                    dfs(i)
        
        for i in range(1,len(isConnected) + 1):
            if i not in visited:
                dfs(i)
                res += 1
        return res
            
         