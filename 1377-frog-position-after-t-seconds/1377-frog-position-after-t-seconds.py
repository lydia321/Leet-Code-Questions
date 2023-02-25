class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = {1: []}
        for n1, n2 in edges:
            if n1 not in graph:
                graph[n1] = []
            graph[n1].append(n2)
            if n2 not in graph:
                graph[n2] = []
            graph[n2].append(n1)
            
        visited = {1}
        
        queue = deque([(1, 1, 0)])
        
        while queue:
            curr,possibility, level = queue.popleft()
            if level > t:
                return 0
            children_count = len(graph[curr]) - 1 if curr != 1 else len(graph[curr])
            if (level == t or children_count == 0) and curr == target:
                return possibility
            for child in graph[curr]:
                if child not in visited:
                    visited.add(child)
                    queue.append((child, possibility / children_count, level + 1))
        
        return 0