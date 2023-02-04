class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        graph = {}
        for i in range(len(arr)):
            if arr[i] != 0:
                graph[i] = []
                if i + arr[i]  <= len(arr) - 1:
                    graph[i].append(i + arr[i])
                if i - arr[i] >= 0:
                    graph[i].append(i - arr[i])
        # print(graph)
        queue = [start]
        visted = {start}
        
        while queue:
            curr = queue.pop(0)
            if arr[curr] == 0:
                return True
            for i in graph[curr]:
                if i not in visted:
                    queue.append(i)
                    visted.add(i)
        return False
                    
            
        