class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        i = 0
        
        for each in costs:
            if (coins - each >= 0):
                coins -= each
                res += 1
            else:
                break
        return res