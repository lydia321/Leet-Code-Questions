class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
    
        """
   # O(n) time comlexity     
        #last index of nums1
        last_idx=len(nums1)-1
        #while both nums have value
        while m > 0 and n > 0:
            if nums1[m-1]>nums2[n-1]:
                nums1[last_idx]=nums1[m-1]
                m-=1
            else: #if they less than or equal
                nums1[last_idx]=nums2[n-1]
                n-=1
            last_idx-=1
        #if there are leftover elements in nums2
        while n>0:
            nums1[last_idx]=nums2[n-1]
            last_idx-=1
            n-=1
            
      # 2)  O(nlogn)  
    
        #del nums1[:m]
        #nums1.extend(nums2)
        #nums2.sort()
        
            
                
                
                
            
          