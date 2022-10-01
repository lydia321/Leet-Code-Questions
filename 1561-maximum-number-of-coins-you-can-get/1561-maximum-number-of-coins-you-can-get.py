class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        r = len(piles) - 2
        rounds = len(piles) // 3
        total = 0
        
        for _ in range(rounds):
            total += piles[r]
            r -= 2
            
        return total
            
            