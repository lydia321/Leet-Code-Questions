class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.backTracking(s,0,seen)
    
    def backTracking(self,s, start, seen):
        if start == len(s):
            return 0

        maxCount = 0

        for end in range(start + 1, len(s)+1):
            subString = s[start:end]

            if subString not in seen:
                seen.add(subString)
                maxCount = max(maxCount, 1 + self.backTracking(s,end,seen))
                seen.remove(subString)

        return maxCount
                
        
        
        

            
            
            
                
            
        
        