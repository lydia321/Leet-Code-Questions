class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1,s2 = [] ,[]
        

        for i in s:
            if i != '#':
                s1.append(i)  
            else:
                if s1:
                    s1.pop()        
        for i in t:
            if i != '#':
                s2.append(i)  
            else:
                if s2:
                    s2.pop()
                
        
        result = True if s1 == s2 else False
        
        return result
                
            
            
            
            
            
            
            
        