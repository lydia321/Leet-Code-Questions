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
                
            
                       
        
     