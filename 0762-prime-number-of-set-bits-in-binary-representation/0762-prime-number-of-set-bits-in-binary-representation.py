class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for i in range(left, right + 1):
            val = bin(i).count('1')
            if val in primes:
                res += 1
        return res
        