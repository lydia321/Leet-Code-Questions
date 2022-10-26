class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        stack = []
        
        for i in a:
            while stack and stack[-1] > 0 and i < 0:
                if abs(i) < stack[-1]:
                    break
                elif abs(i)==stack[-1]:
                    stack.pop()
                    break
                else:
                    stack.pop()
            else:
                stack.append(i)
        return stack  
       
           
                
              
        