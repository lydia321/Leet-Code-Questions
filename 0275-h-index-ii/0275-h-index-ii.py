class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations)-1
        if len(citations) == 0:
            return 0
        
        while l < r:
            m = (l+r)//2
            if len(citations) - m <= citations[m]:
                r = m 
            else:
                l = m + 1
        
        if citations[l] == 0:
            return 0
        return len(citations) - r

    