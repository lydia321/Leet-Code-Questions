class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSub = 0
        
        for n in nums:
            #if our currSub becomes -ve, reset back to 0,disregared those prefixes
            if currSub < 0:
                currSub = 0
            currSub += n
            maxSub = max(currSub,maxSub)
            print(maxSub)
        return maxSub
#         arr=[0]*len(nums) #array of 0's *length
#         arr[0]=nums[0]  #add first element to start with
        
#         for i in range(1,len(nums)): 
#             if arr[i-1] > 0:  #look at the value of last index of arr, 
#                 arr[i]=nums[i]+arr[i-1]
#             else:
#                 arr[i]=nums[i]
                
#         return max(arr)   
    
    
# #                 '''
# #                  [5,4,-1,7,8]
# #                  [0,0,0,0,0]
# #                  [5,0,0,0,0]
# #                  [5,9{4+5},0,0,0]
# #                  [5,9,8{9+-1},0,0]
# #                  [5,9,8,15{8+7},0]
# #                  [5,9,8,15,23{15+8}]
# #                   max=23
                 
                 
# #                 '''
#         '''
#         [0,0,0,0,0,0,0,0,0,0,0]
#         [-2,1,-3,4,-1,2,1,-5,4]
        
#         [-2,1,-2,4,3,5,6,1,5] 
        
        
#         '''
                       
        
     