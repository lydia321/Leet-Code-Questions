class Solution:
    def findMinHeightTrees(self, n: int, edge: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        edges = defaultdict(int)  
        #if graph only has two nodes
        if n <= 2:
            return list(range(n))
        
        for i in edge:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            edges[i[0]] += 1
            edges[i[1]] += 1
        queue = []
        # print(graph,edges)
        for i in edges:
            if edges[i] == 1:
                queue.append(i)
        current_count = n
        while current_count > 2:
            current_count -= len(queue)
            temp_res = []
            while queue:
                for _ in range(len(queue)):
                    curr = queue.pop()
                                        
                    #Since curr has only one edge
                    only_nei = graph[curr].pop()
                    #remove curr from its only nei also
                    graph[only_nei].remove(curr)
                    if len(graph[only_nei]) == 1:
                        temp_res.append(only_nei)
            queue = temp_res
                        
            
        return queue
              