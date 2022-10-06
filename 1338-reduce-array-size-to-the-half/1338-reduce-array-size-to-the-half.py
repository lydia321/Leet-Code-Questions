from collections import Counter 
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr).values()
        counts = sorted(counts, reverse=True)
        
        Numbers_to_be_substracted = 0
        set_size_to_be_substracted = 0
        
        for i in counts:
            if set_size_to_be_substracted < len(arr)//2:
                Numbers_to_be_substracted += 1
                set_size_to_be_substracted += i
                
        return Numbers_to_be_substracted      
                
                
            
            
        
        
        
            
            
            
        
        
        
        