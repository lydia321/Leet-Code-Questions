class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        a,b,c = 0,0,[]
        
        for i in range(len(s)):
            if s[i] == "(":
                a = a+1
            else:
                a = a-1
            if a == 0:
                c.append(s[b:i+1])
                b = i+1

          
        output = []
        for i in range(len(c)):
            a= c[i]
            output.append(a[1:-1])
        return "".join(output)            
            
                    
        
                
        