class Solution:
    def reverseWords(self, s: str) -> str:
        curr = ''
        res = ''
        
        for r in range(len(s)):
            if s[r] != " ":  curr = s[r] + curr
            else:
                res += curr
                res += " "
                curr = ''
        l = s.split(" ")[-1][::-1]
        return res + l