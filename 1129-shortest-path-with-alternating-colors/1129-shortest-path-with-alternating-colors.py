from collections import defaultdict

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Create adjacency lists for red and blue edges
        red = defaultdict(list)
        blue = defaultdict(list)
        
        # Populate the adjacency lists
        for i, j in redEdges:
            red[i].append(j)
        
        for i, j in blueEdges:
            blue[i].append(j)
        
        # Initialize result list with -1 (unreachable)
        res = [-1] * n
        res[0] = 0  # The distance to the start node is 0
        
        # Initialize BFS queue with two possible starting points
        queue = [(0, 0, "Red"), (0, 0, "Blue")]  # (node, distance, last color used)
        visited = set()  # Track visited nodes with their color
        
        while queue:
            node, dist, last_color = queue.pop(0)
            
            # Explore red edges if the last color was not red
            if last_color != "Red":
                for neighbor in red[node]:
                    if (neighbor, "Red") not in visited:
                        visited.add((neighbor, "Red"))
                        queue.append((neighbor, dist + 1, "Red"))
                        if res[neighbor] == -1 or res[neighbor] > dist + 1:
                            res[neighbor] = dist + 1
            
            # Explore blue edges if the last color was not blue
            if last_color != "Blue":
                for neighbor in blue[node]:
                    if (neighbor, "Blue") not in visited:
                        visited.add((neighbor, "Blue"))
                        queue.append((neighbor, dist + 1, "Blue"))
                        if res[neighbor] == -1 or res[neighbor] > dist + 1:
                            res[neighbor] = dist + 1
        
        return res
