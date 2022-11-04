class Solution:
    def reverseVowels(self, c: str) -> str:
        s: list[str]=list(c)
        l,r = 0,len(s)-1
        d = ['a','e','i','o','u','A','I','O','U','E']
        
        
        
      
        while l < r:
             if s[l] not in d:
                    l += 1

             else:
                if s[r] not in d:
                    r -= 1
                else:
                    if s[r] != s[l]:
                        s[r],s[l] = s[l],s[r]
                        l += 1
                        r -= 1
                    else:
                        l += 1
                        r -= 1
                        
                        
        return "".join(s)                 
                    
                
             
             
             
             
             
             
             
            
            
            
        