class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,pos = [nums[0]], [nums[-1]]
        
        for i in range(1,len(nums)):
            pre.append(nums[i]*pre[-1])
        
        for i in range(len(nums)-2,-1,-1):
            pos.append(nums[i]*pos[-1])
        pos = pos[::-1]
        print(pos)
        print(pre)
        output = [pos[1]]
        for i in range(1,len(nums)-1):
            output.append(pre[i-1]*pos[i+1])
        output.append(pre[-2])
        return output    
            
        
            
        