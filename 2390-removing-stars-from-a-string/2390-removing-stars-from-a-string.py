class Solution:
    def removeStars(self, s: str) -> str:
        star = '*'
        stack = []
        
        for i in s:
            if i != star:
                stack.append(i)
            else:
                stack.pop()
        
        output = "".join(stack)
        return output    
        
        