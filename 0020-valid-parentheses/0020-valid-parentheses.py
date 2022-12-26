class Solution:
    def isValid(self, s: str) -> bool:
        lookup = { '}' : '{' , ']' : '[' , ')' : '('}
        openings = lookup.values()
        stack = [s[0]]
            
        for i in range(1, len(s)):
            if s[i] in openings:
                stack.append(s[i])
            else:
                if stack and stack[-1] == lookup[s[i]]:
                    stack.pop()
                else:
                    return False  
        return len(stack) == 0