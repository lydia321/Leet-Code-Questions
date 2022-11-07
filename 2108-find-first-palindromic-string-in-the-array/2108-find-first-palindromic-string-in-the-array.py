class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res  = ''
        for i in words:
            curr = i[::-1]
            if i == curr:
                res = res + i
                break
        return res        
                
        