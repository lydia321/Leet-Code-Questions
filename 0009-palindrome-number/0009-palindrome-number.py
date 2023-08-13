class Solution:
    def isPalindrome(self, x: int) -> bool:
        output=[]
        if x < 0:
            return False
        for i in str(x):
            output.append(int(i))
        l=0
        r=len(output)-1
        while l < r:
            if output[l]!=output[r]:
                return False
            l+=1
            r-=1
        return True    
           
           
            
           
        