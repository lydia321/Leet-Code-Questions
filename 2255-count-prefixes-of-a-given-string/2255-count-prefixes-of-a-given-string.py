class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        
        for i in words:
            curr = s[:len(i)]
            if curr == i:
                res  += 1
        return res