class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ''
        
        
        for i in range(len(palindrome)//2):
            if palindrome[i] != 'a':
                return palindrome.replace(palindrome[i],'a',1)
        
        # If the sting was all a's
        for i in range(len(palindrome)-1,-1,-1):
            # print(palindrome[i])
            curr = palindrome.replace(palindrome[i],'b',1)
               
            return curr[::-1]
        return ''