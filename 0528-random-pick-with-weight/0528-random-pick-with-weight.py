class Solution:

    def __init__(self, w: List[int]):
        self.prefixSum = list(accumulate(w))

    def pickIndex(self) -> int:
        target = random.random()*self.prefixSum[-1]
        l , r = 0 , len(self.prefixSum) - 1 
        
        while l <= r:
            m = l + ( r - l)//2
            
            if target > self.prefixSum[m]:
                l = m + 1
            else:
                r = m - 1
        
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
