"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        for i in employees:
            graph[i.id] = i
        # print(graph)
        self.res = 0
        
        def dfs(root):
            # print(root)
            self.res += root.importance
            for i in root.subordinates:
                dfs(graph[i])
        
        for i in graph:
            print(i)
            if graph[i].id == id:
                dfs(graph[i])
        
        
        return self.res
        
                