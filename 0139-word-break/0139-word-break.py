class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[len(s)] = True
        
        def match(i,each_word):
            curr_word = s[i:i+len(each_word)]
            if curr_word == each_word:
                dp[i] = dp[i + len(each_word)]
            
        
        for i in range(len(s)-1,-1,-1): 
            for each_word in wordDict:
                match(i,each_word)
                if dp[i] == True:
                    break
                else:
                    match(i,each_word)
        return dp[0]
                    
         