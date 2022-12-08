class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lookup = {}
        stack = []
        
        for i in range(len(s)):
            lookup[s[i]] = i
       
        
        for i in range(len(s)):
            if s[i] not in stack:
                while stack and stack[-1] > s[i] and lookup[stack[-1]] > i:
                    stack.pop()
                stack.append(s[i])
        return "".join(stack)
        