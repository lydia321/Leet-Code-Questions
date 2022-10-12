class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lookup = set(nums)
        output = []
        
        for i in range(1,len(nums)+1):
            if i not in lookup:
                output.append(i)
             
        return output    
                
        