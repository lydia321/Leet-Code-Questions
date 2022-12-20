class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = 0
        dict = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        lookup = []
        for word in words:
            curr = ''
            for j in word:
                curr += dict[ord(j) - ord('a')]
            if curr not in lookup:
                lookup.append(curr)
                res += 1
        return res
                