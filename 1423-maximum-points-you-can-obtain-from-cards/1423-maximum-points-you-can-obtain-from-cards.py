class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0 
        r = len(cardPoints) - k
        curr = sum(cardPoints[r:])
        res = curr
        
        #Sliding Window
        while r < len(cardPoints) :
            curr += cardPoints[l]
            curr -= cardPoints[r]
            
            res = max(res,curr)
            l += 1
            r += 1
        return res
            
        
        
        
        