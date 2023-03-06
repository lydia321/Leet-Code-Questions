class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        graph = set()
        
        for a,b in edges:
            graph.add(b)
        # print(graph,res)
        for i in range(n):
            if i not in graph:
                res.append(i)
        return res
            
            