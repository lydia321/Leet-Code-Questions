class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack:
                if i != stack[-1]:
                    stack.append(i)
                else:
                    stack.pop()
                    
            else:
                stack.append(i)
        
        output = ''.join(stack)
        return output
        