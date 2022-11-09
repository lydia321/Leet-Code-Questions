class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        m = len(s)//2
        s1= s[:m]
        s2 = s[m:]
        
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        a=b=0
        for i in s1:
            if i in vowel:
                a += 1
        
        for i in s2:
            if i in vowel:
                b += 1  
        print(s2)
        return True if a== b else False        
        