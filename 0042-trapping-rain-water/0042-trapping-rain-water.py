class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0]
        for i in range(len(height)-1):
            leftMax.append(max(leftMax[-1],height[i]))
        
        rightMax = [0]
        for i in range(len(height)-1,0,-1):
            rightMax.append(max(rightMax[-1],height[i]))
        rightMax = rightMax[::-1]
        
        CurrMaxHeight , currValue , res = 0 , 0 , 0
        for i in range(len(height)):
            CurrMaxHeight = min(leftMax[i],rightMax[i])
            currValue = CurrMaxHeight - height[i]
            if currValue > 0:
                res += currValue
        print(leftMax,rightMax, CurrMaxHeight)
        return res
                
            