class Solution:
    #checking if its a nice array
    def checkNice(self, s: str) -> bool:
        for i in s:
            if i.swapcase() not in s:
                return False
        return True

    def longestNiceSubstring(self, s: str) -> str:
        res = ""

        if len(s) < 2:
            return ""
       
        if self.checkNice(s):
            return s

        for l in range(len(s)):
            
            for r in range(l+1, len(s)):
                
                if self.checkNice(s[l:r+1]):
                    
                    if len(res) < len(s[l:r+1]):
                        res = s[l:r+1]
        return res 
        