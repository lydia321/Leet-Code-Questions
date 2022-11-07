class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for i in s:
            if re.match('^[a-zA-Z0-9]+$',i):
                res = res + i.lower()
        if res == res[::-1]:
            return True
        return False
    
        
        