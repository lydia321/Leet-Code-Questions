class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        
        for i in words:
            curr = i[:len(pref)]
            if curr == pref:
                res += 1
        return res