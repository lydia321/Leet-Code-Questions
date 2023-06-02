class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        dict = defaultdict(list)
        
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x1 - x2)**2 + (y1 - y2)**2)
                
                if d <= r1:
                    dict[i].append(j)
                    
                if d <= r2:
                    dict[j].append(i)
        
        def dfs(i,visited):
            #base case 
            if i in visited:
                return 0
            visited.add(i)
            for neg in dict[i]:
                dfs(neg,visited)
            return len(visited)
        
        res = 0        
        for i in range(len(bombs)):
            res = max(res,(dfs(i,set())))  
        return res
                    
                