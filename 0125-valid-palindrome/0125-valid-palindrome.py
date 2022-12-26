class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        res2 = ""
        
        for i in s:
            if i.isalnum():
                res = res + i.lower()
                res2 = i.lower() + res2
        print(res,res2)
        if res == res2:
            return True
        return False
        
        