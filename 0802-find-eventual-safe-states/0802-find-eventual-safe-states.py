class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph_ = {}
        for i in range(len(graph)):
            graph_[i] = graph[i]
        print(graph_)
        res = []
        visited = set()
        
        def dfs(root):
            if graph_[root] == [] :
                return True
            if root in visited:
                return False
            visited.add(root)
            for j in graph_[root]:
                if not dfs(j):
                    return False
            visited.remove(root)
            graph_[root] = []
            return True
        
        for i in graph_:
            if dfs(i) and i not in res: 
                res.append(i)
        return sorted(res)
            