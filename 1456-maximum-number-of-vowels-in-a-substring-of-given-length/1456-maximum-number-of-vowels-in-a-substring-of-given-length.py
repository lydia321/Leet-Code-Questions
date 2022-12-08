class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr = l = 0
        vowel = 'aeiou'
        total = s[0:k]
        
        for i in total:
            if i in vowel: curr += 1
        
        res = curr
      
        for r in range(k,len(s)):
            
            if s[r] in vowel:curr += 1
                
            if s[l] in vowel: curr -= 1
            
            l += 1
            res = max(curr,res)
        return res
        
        