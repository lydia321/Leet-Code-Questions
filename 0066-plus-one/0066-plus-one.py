class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s,output = [], []
        
        for i in digits:
            s.append(str(i))
        
        s=''.join(s)
        res = int(s) + 1
        
        for i in str(res):
            output.append(int(i))
        return output    
          
            
            