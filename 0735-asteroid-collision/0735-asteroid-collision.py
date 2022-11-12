class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        stack = []
        
        for i in a:
            while stack and stack[-1] > 0 and i < 0:
                if stack[-1] > abs(i):
                    i = 0
                elif stack[-1] < abs(i):
                    stack.pop()
                else:
                    stack.pop()
                    i = 0
            if i < 0 or i > 0:
                stack.append(i)
        return stack
                    
        
          
       
           
                
              
        