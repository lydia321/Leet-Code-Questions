class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        rounds=len(piles) // 3
        
        r= len(piles) - 2
        count=0
        
        for i in range(rounds):
            count +=piles[r]
            r-=2
        
        return count
            
            
        
            
            