class Solution(object):
    def hIndex(self, citations):
        c=reversed(sorted(citations))
        for i,val in enumerate(c):
            if i>=val:
                return i
        return len(citations)
            
                
                
                
      
        