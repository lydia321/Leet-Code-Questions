class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        () (()), ((
        (())
        )()())
        
        )()())()   4
        )))
        (()
        
        '''
        res = 0
        stack = [-1]
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                # if i popped the last valid index
                if not stack:
                    stack.append(i) #add new valid index
                else:
                    res = max(res,i - stack[-1])
                    
        return res
        
                
        
        
      