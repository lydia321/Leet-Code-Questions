class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        E=[]
        O=[]
        output=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                E.append(nums[i])
            else:
                O.append(nums[i])
        for i in range(len(E)):
            output.append(E[i])
            output.append(O[i])
        return output    
        
    
                