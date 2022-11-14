class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        
        curr = 0
        
        for i in s:
            if i.isalpha(): 
                curr += 1
                
            else:
                curr *= int(i)

        for i in reversed(s):
            k %= curr
            if i.isalpha():
                curr -= 1
            else:
                curr /= int(i)
            
            if k == 0 and i.isalpha():
                return i
                
         
        
        