class Solution:
    def reverse(self, x: int) -> int:
        
        neg = 0
        
        # convert to string
        x = str(x)
        
        if x[0] == "-":
            neg = 1
            x = x[1:]
        
        # reverse string
        x = x[::-1]
        
        # convert to integer
        x = int(x)
        if neg == 1:
            x = -x
        
        return x if (x >= -2**31) and (x <= (2**31)-1) else 0
           
                
        
            
            
            
            
            
            
        