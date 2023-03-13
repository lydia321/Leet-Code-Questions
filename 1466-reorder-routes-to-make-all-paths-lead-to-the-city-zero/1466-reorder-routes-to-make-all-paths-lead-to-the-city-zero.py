class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for frm, to in connections:
            graph[frm].append((to, 'from'))
            graph[to].append((frm, 'to'))
            
            '''
            0: (1, from), (4, to)
            1: (0, to), (3, from)
            3: (1, to), (2, to)
            2: (3, from)
            4: (0, from), (5, from)
            5: (4, to) 
            bfs(0), 2
            '''
        self.res = 0
        visited = set()
        
        def dfs(root):
            visited.add(root)
            
            for i in graph[root]:
                if i[0] not in visited:
                    if i[1] == 'from':
                        self.res += 1
                    dfs(i[0])
                    
        
        dfs(0)
        return self.res
    
#         queue = [0]
#         visited = set()
#         res = 0
        
#         while queue:
#             for  _ in range(len(queue)):
#                 curr = queue.pop(0)
                
#                 for i in graph[curr]:
#                     if i[0] not in visited: 
#                         queue.append(i[0])
#                         visited.append(i[0])
    #                     if i[1] == 'from':
    #                             res += 1
#         return res
        