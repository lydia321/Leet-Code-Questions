class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        a = s.split(" ")
        print(a)
        res = ""
        
        for i in range(k):
            res += a[i] +" "
        return res[:-1]