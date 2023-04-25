class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for i in s:
            if stack and stack[-1] == "[" and i == "]":
                stack.pop()
            else:
                stack.append(i)
        res = max(stack.count('['),stack.count(']'))
        return (res + 1) // 2
        
        