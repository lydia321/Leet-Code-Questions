class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import math
        nums1.extend(nums2)
        nums1.sort()
        m= len(nums1)/2
        rm=math.ceil(m)
        
        idx=rm-1
        
        for i in range(len(nums1)):
            if len(nums1)%2!=0:
                return nums1[idx]
            else:
                sum_=nums1[rm]+nums1[rm-1]
                return (sum_/2)
                
                
           
            
        
        