class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[0]:
                popped.pop(0)
                stack.pop()
            if len(popped) == 0:
                return True
        return False