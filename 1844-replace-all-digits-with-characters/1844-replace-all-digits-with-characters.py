class Solution:
    def replaceDigits(self, s: str) -> str:
        output = ''
        
        for i in range(len(s)):
            if s[i].isnumeric():
                output += chr(ord(s[i-1])+int(s[i]))
            else:
                output += s[i]
        return output        
        