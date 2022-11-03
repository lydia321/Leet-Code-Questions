class Solution:
    def frequencySort(self, s: str) -> str:
        a  = Counter(s)
        res = '' 
        
        for i,c in a.most_common():
            res = res + i*c
                
        return str(res)   
        
        