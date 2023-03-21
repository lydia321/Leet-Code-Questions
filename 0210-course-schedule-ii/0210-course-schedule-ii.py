class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for i in prerequisites:
            graph[i[0]].append(i[1])
        res = []
        visited = set()
        
        def dfs(root):
            if graph[root] == []:
                if root not in res: res.append(root)
                return True
            if root in visited:
                return False
            visited.add(root)
            for i in graph[root]:
                if not dfs(i):
                    return False
            visited.remove(root)
            if root not in res: res.append(root)
            graph[root] = []
            return True
            
        for i in graph:
            if not dfs(i):
                return []
        return res
#         graph = defaultdict(list)
#         for i in prerequisites:
#             graph[i[1]].append(i[0])
#         res = []
#         queue = [0]
#         visited = set()
        
#         while queue:
            
#             for _ in range(len(queue)):
#                 curr = queue.pop(0)
                
#                 if curr in visited:
#                     return []
#                 visited.add(curr)
#                 res.append(curr)
#                 for i in graph[curr]:
#                     queue.append(i)
#         return res
                
                
                
        
        