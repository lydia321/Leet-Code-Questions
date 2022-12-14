class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        
        for i in range(0,len(s),k+k):
            curr = s[i:i+k+k]
            res += curr[0:k][::-1] + curr[k:]
        return res
        
        