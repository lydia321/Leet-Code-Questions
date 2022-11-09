class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r =0
        steps = 0
        
        while r <len(nums) -1:
            a = 0
            for i in range(l,r+1):
                a = max(a,nums[i]+i)
            l = r+1
            r = a
            steps += 1
        return steps    
            
            
        