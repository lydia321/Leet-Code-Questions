class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.end = len(graph) - 1
        
        def dfs(root,curr_path):
            if root == self.end:
                self.res.append(curr_path)
            
            for i in graph[root]:
                dfs(i, curr_path + [i])
            
        dfs(0,[0])
        return self.res