class Solution:
    def reverseWords(self, s: str) -> str:
        r = s.split()
        r = r[::-1]
        return " ".join(r)