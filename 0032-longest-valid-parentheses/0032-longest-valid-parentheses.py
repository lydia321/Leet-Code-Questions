class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = []
        
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(-1)
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res,i - stack[-1])
        return res
                
        
        
        
#         count = 0
#         stack = []
        
#         for i in s:
#             if len(stack) == 0:
#                 if i == "(":
#                     stack.append(i)
#                 else:
#                     continue
#             elif stack[-1] == '(':
#                 if i == "(":
#                     stack.append(i)
#                 else:
#                     stack.pop()
#                     count += 2
#             else:
#                 continue
#         return count
       