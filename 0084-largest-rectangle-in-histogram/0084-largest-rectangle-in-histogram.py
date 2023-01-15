class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # index,height
        maxArea = 0
        
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                curridx,currheight = stack.pop()
                maxArea = max(maxArea,currheight*(i - curridx))
                start = curridx
            stack.append((start,h))
        
        #remaining heights in stack
        for i,h in stack:
            maxArea = max(maxArea,h*(len(heights) - i))
        return maxArea
    
        
        
    