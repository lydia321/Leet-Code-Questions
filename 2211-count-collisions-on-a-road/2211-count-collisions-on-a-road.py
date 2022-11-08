class Solution:
    def countCollisions(self, direction: str) -> int:
        count = 0
        directions = collections.deque(list(direction))
        print(directions)
        for i in directions:
            if i == 'S':
                count += 1
        
        while len(directions)>0 and directions[0] == 'L':
            directions.popleft()
        while len(directions)>0 and directions[-1] == 'R':
            directions.pop()
        
        return len(directions)-count
            
            