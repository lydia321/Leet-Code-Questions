class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        output = ''
        
        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][1] += 1
            else:
                stack.append([i,1])
                
            if stack[-1][1] == k:
                stack.pop()
         
        for i,count in stack:
            output += (i*count)
            
        return output    
                
        
            
                
        
        
            
            
                
                
            