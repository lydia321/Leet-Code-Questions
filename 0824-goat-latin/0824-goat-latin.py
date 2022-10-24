class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        word = sentence.split()
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        a = 1
        
        for i in range(len(word)):
            if word[i][0] in vowel:
                word[i] = word[i] + "ma"
            else:
                word[i] = word[i][1:] + word[i][0]
                word[i] = word[i] + 'ma'
            word[i] = word[i] + 'a'*a 
            a +=1
        return " ".join(word)    
                
        