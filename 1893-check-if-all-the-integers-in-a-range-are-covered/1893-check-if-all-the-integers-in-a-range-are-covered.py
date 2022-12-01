class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans = 0
        
        for i in range(left,right+1):
        
            for x,y in ranges:
                if x<=i and i <= y:
                    ans += 1
                    break
        return ans==(right-left)+1