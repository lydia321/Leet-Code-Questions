class Solution:
    def findMinHeightTrees(self, n: int, edge: List[List[int]]) -> List[int]:
        #if there are less than 2 nodes:
        if n < 3:
            return list(range(n))
        
        graph = defaultdict(list)
        edges = defaultdict(int)
        
        for i in edge:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            edges[i[0]] += 1
            edges[i[1]] += 1
        # print(graph, edges)
        queue = []
        for i in edges:
            if edges[i] == 1:
                queue.append(i)
        # print(queue)
        remaining_count = n
        
        while remaining_count > 2:
            possible_res = []
            while queue:
                for _ in range(len(queue)):
                    remaining_count -= 1
                    curr = queue.pop(0)
                    # since it only has one neighbour
                    only_nei = graph[curr].pop()
                    graph[only_nei].remove(curr)
                    edges[only_nei] -= 1
                    edges[curr] -= 1
                    if len(graph[only_nei]) == 1:
                        possible_res.append(only_nei)
            queue = possible_res
        return queue
                    
                    