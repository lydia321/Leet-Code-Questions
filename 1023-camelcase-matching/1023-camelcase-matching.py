class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for word in queries:
            i = 0
            flag = True
            for c in word:
                if i < len(pattern) and c == pattern[i]:
                    i += 1
                elif c.islower():
                    continue
                else:
                    flag = False
                    break
            if i != len(pattern) :
                flag = False
            res.append(flag)
                
        return res