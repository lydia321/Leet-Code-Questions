class Solution:
    def getAncestors(self, n: int, edge: List[List[int]]) -> List[List[int]]:
        graph,edges,res = {}, {}, []
        for i in range(n):
            graph[i] = []
            res.append(set())
            edges[i] = 0
        
        for i in edge:
            graph[i[0]].append(i[1])
            edges[i[1]] += 1
        
        queue = []
        for i in edges:
            if edges[i] == 0:
                queue.append(i)
        
        
        while queue:
            
            for _ in range(len(queue)):
                curr = queue.pop(0)
                
                for i in graph[curr]:
                    edges[i] -= 1
                    res[i].add(curr)
                    res[i] |= res[curr]
                    if edges[i] == 0:
                        queue.append(i)
        final = []
        # print(graph,edges,res,queue)
        for i in res:
            final.append(list(sorted(i)))
        return final