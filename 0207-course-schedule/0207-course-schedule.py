class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        visited = set()
        
        for i in range(numCourses):
            if i not in graph:
                graph[i] = []
        for i in prerequisites:
            graph[i[0]].append(i[1])
        print(graph)
        
        def dfs(root):
            if graph[root] == []:
                return True
            if root in visited:
                return False
            visited.add(root)
            for j in graph[root]:
                if not dfs(j):
                    return False
            visited.remove(root)
            graph[root] = []
            return True
            
        
        for i in graph:
            if not dfs(i):
                return False
        return True
       