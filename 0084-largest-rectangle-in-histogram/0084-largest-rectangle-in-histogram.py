class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        
        for i,h in enumerate(heights):
            startWidth = i
            while stack and stack[-1][1] > h:
                curridx,currheight = stack.pop()
                maxArea = max(maxArea, currheight *(i - curridx))
                startWidth = curridx
            stack.append((startWidth,h))
            
        for i,h in stack:
            maxArea = max(maxArea,h *(len(heights) - i))
        return maxArea
    
        
        
    