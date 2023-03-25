class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        edges = defaultdict(int)
        has = set(supplies)
        
        for i in range(len(ingredients)):
            for j in ingredients[i]:
                if j not in has:
                    edges[recipes[i]] += 1
                    graph[j].append(recipes[i])
        # print(graph)
        # print(edges)
        queue = []
        for i in recipes:
            if edges[i] == 0:
                queue.append(i)
        res = []
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop()
                res.append(curr)
                
                for i in graph[curr]:
                    edges[i] -= 1
                    if edges[i] == 0:
                        queue.append(i)
        return res