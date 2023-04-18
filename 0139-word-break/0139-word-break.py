class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[len(s)] = True      
        for i in range(len(s)-1,-1,-1):
            for each in wordDict:
                curr = s[i:i+len(each)]
                if curr == each:
                    dp[i] = dp[i + len(each)]
                if dp[i] : 
                    break
        return dp[0]
                    
            