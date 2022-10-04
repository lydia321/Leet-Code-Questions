class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = defaultdict(int)
        stack=[]
        output=[-1] * len(nums1)
        
        for i,val in enumerate(nums1):
            lookup[val] = i
         
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                temp = stack.pop()
                output[lookup[temp]] = nums2[i]
                    
            if nums2[i] in lookup: stack.append(nums2[i])
                
        return output