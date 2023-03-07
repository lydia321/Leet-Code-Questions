class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        res = 0
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected[i])):
                if isConnected[i][j]:
                    graph[i+1].append(j+1)
                    graph[j+1].append(i+1)
        print(graph)
        
        def dfs(root):
            if root in visited: 
                return False
            
            visited.add(root)
            for ne in graph[root]:
                dfs(ne)
            return True
            
        
        for i in range(1, len(isConnected)+1):
            if i not in visited and dfs(i):
                res += 1
        return res
                
