class Solution:
    def canWinNim(self, n: int) -> bool:
        r = n%4
        return True if r != 0 else False
        