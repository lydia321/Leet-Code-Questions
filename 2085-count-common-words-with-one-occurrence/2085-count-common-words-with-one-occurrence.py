class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        A = Counter(words1)
        B = Counter(words2)
        # print(A,B)
        res = 0
        for val,count in A.items():
            if count == 1 and val in B and B[val] == 1 :
                res += 1
        return res
            