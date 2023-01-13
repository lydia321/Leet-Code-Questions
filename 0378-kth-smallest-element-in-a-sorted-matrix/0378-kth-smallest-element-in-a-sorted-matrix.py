class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        stack = []
        for i in matrix:
            stack.extend(i)
        print(stack)
        stack.sort()
        return stack[k-1]