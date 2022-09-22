class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr=[0]*len(nums)
        arr[0]=nums[0]
        
        for i in range(1,len(nums)):
            if arr[i-1] > 0:
                arr[i]=nums[i]+arr[i-1]
            else:
                arr[i]=nums[i]
                
        return max(arr)      
                
            
                       
        
        '''
        -2 1 -3 4
        
        -2
        -2 1
        -2 1 -3
        -2 1 -3 4
        1
        1 -3
        1 -3 4
        -3
        -3 4
        4
        
        
        4
        '''