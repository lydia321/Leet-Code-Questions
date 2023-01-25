class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = [] #open parentheses, index
        res = list(s)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append([s[i],i])
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    res[i] = ''     
        #for open parentheses that arent closed
        if stack:
            for i in stack:
                res[i[1]] = ''
        
        return ''.join(res)
            