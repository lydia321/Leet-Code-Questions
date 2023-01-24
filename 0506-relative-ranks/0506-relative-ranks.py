class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        A = sorted(score, reverse = True)
        res = []
        for i,val in enumerate(score):
            if A.index(val) == 0:
                res.append("Gold Medal")
            elif A.index(val) == 1:
                res.append("Silver Medal")
            elif A.index(val) == 2:
                res.append("Bronze Medal")
            else:
                res.append(str(A.index(val)+1))
        return res