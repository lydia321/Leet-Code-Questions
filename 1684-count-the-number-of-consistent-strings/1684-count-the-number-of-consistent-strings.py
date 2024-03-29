class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        
        for word in words:
            flag = True
            for c in word:
                if c not in allowed:
                    flag = False
            if flag:
                res += 1
        return res