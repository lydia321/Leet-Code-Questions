class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=[]
        for i in nums1:
            if i in nums2 and i not in output:
                output.append(i)
        return output        
                
        