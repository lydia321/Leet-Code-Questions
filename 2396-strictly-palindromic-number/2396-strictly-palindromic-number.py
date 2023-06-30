class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        #any number in base 2 is 12 and therefor any number greater than 4 cannot strictky be  palindromic.
        return False