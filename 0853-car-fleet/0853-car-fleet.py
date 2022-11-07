class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        res = []
        
        for c,s in zip(position,speed):
            stack.append([c,s])
            
        for c,s in sorted(stack)[::-1]:  
            
            res.append((target-c)/s)
            if len(res)>1 and  res[-1] <= res[-2]:
                res.pop()
        print(res)    
        return len(res)
    
        