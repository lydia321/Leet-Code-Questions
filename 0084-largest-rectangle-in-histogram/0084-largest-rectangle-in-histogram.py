class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #index, height
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                #pop height
                #Update maxArea
                #extend curr height backwards
                CurrIdx,CurrHeight = stack.pop()
                width = i - CurrIdx
                maxArea = max(maxArea,(CurrHeight * width))
                start = CurrIdx
            stack.append((start,h))
        
        #remaining heights in our stack
        for i, h in stack:
            width = len(heights) - i
            maxArea = max(maxArea,(h * width))
        
        return maxArea
    