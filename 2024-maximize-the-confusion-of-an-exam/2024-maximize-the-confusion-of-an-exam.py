class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0
        res = 0
        curr = {}
        
        for r in range(len(answerKey)):
            curr[answerKey[r]] = 1 + curr.get(answerKey[r],0)
            
            while ((r - l + 1) - max(curr.values())) > k:
                curr[answerKey[l]] -= 1
                if curr[answerKey[l]] == 0: curr.pop(answerKey[l])
                l += 1
            res = max(res,r - l + 1)
        return res
            
        