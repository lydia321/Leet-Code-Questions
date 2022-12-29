class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = sentence.split(" ")
        
        for i in range(len(s)):
            if searchWord in s[i]:
                curr = s[i][:len(searchWord)]
                if curr == searchWord:
                    return i + 1
                    break
        return -1
    