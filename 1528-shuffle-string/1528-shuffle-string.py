class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        idx = 0
        res = [0]*len(s)
        
        for i in s:
            j = indices[idx]
            res[j] = i
            idx += 1
        return "".join(res)    
            
            
            
            
            
            