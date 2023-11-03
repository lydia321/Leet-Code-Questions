class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                curr = ''
                while stack[-1] != '[':
                    val = stack.pop()
                    curr += val
                stack.pop()
                n = ''
                while stack and stack[-1].isdigit():
                    n += stack.pop()
                res = curr * int(n[::-1])
                stack.append(res)
        final = ''
        for i in stack:
            final += i[::-1]
        return final
    
        