class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        temp = []
        a = 0
        start = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                a += 1
            else:
                a -= 1
            if a == 0:
                temp.append(s[start:i+1])
                start = i+1
        
        output = [] 
        for i in temp:
            output.append(i[1:-1])
        return "".join(output)    
            
                
                
            
                    
        
                
        