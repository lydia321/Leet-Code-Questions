class Solution:
    def digitCount(self, num: str) -> bool:
        
        for i in range(len(num)):
            c = num.count(str(i))
            print(c)
            if int(num[i]) != c:
                return False
        return True
            
            
            
            
        