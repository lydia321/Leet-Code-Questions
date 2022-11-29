class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        stack = [0]
        for i in gain:
            stack.append(stack[-1]+i)
        return max(stack)
            
        