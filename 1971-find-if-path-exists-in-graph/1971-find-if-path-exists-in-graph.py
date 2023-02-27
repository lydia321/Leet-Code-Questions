class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #DFS
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        print(graph)
        visited = set()
        
        def dfs(root):
            visited.add(root)
            if root == destination:
                return True
            for i in graph[root]:
                if i not in visited and dfs(i) == True:
                    return True
                
            return False
        return dfs(source)
        
        
        #BFS 
#         graph = defaultdict(list)
#         for i in edges:
#             graph[i[0]].append(i[1])
#             graph[i[1]].append(i[0])
#         # print(graph)
#         queue = [source]
#         visited = set({source})
        
#         while queue:
#             curr = queue.pop(0)
#             if curr == destination:
#                 return True
#             for i in graph[curr]:
#                 if i not in visited:
#                     visited.add(i)               
#                     queue.append(i)
#         return False
       