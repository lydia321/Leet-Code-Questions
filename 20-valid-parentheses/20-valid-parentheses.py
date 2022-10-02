class Solution:
    def isValid(self, s: str) -> bool:
        lookup = { '}' : '{' , ']' : '[' , ')' : '('}
        stack = []
        stack.append(s[0])
        i = 1
        
        while i < len(s):
            if s[i] in lookup.values():
                stack.append(s[i])
            else:
                if stack and stack[-1] == lookup[s[i]]:
                    stack.pop()
                else:
                    return False
            i+=1    
        if stack == []:
            return True
        else:
            return False