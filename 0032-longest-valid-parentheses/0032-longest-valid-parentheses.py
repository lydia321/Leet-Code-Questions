class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        ()
        (())
        ()()
        
        )()())()   4
        01234567
        [5]
        
        )))
        []
        
        '''
        if s == "":
            return 0
        res = 0
        stack = [-1]
        dp = [0]*len(s)
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                j = stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res,i - stack[-1])
                    dp[i] = dp[j - 1] + (i - j + 1)
        return max(dp)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if s == "":
#             return 0
#         res = 0
#         stack = [-1]
#         # dp = [0]*len(s)
        
#         for i in range(len(s)):
#             if s[i] == "(":
#                 stack.append(i)
#                 # dp[0] = 0
#             else:
#                 j = stack.pop()
#                 # if i popped the last valid index
#                 if not stack:
#                     stack.append(i) #add new valid index
#                 else:
#                     res = max(res,i - stack[-1])
#                     # dp[i] = (i - j + 1) + dp[j - 1]
#         return res            
#         # return max(dp)
        
                
        
        
      