class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        stack = []
        
        for i in a:
            while stack and i < 0 and stack[-1] > 0:
                
                if abs(i) == (stack[-1]):
                    stack.pop()
                    break
                elif abs(i) > stack[-1]:
                    stack.pop()
                elif abs(i) < stack[-1]:
                    break   
            else:    
                stack.append(i)
        return stack           
             
       
           
                
              
        