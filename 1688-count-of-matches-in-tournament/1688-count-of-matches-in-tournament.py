class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        count = 0
        temp = []
        
        for _ in range(n):
            num=n//2
           
            count += num
           
            reminder = n - num
            n=reminder
        return count    
            
        