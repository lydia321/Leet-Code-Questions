class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        visited = set()
        for i in range(numCourses):
            graph[i] = []
        for i in prerequisites:
            graph[i[1]].append(i[0])
        
        def dfs(root):
            if root in visited:
                return False
            
            if graph[root] == []:
                return True
            
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