class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = []
        for i in nums1:
            if i in nums2 or i in nums3:
                res.append(i)
        for i in nums2:
            if i in nums1 or i in nums3:
                res.append(i)
        return set(res)
                
#         n2 = {}
#         n3 = {}
#         for i in nums2:
#             n2[i] = 1 + n2.get(i,0)
            
#         for i in nums3:
#             n3[i] = 1 + n3.get(i,0)
#         res = []
#         for i in set(nums1):
#             if i in n2 or i in n3:
#                 res.append(i)
#         for i in nums2:
#             if i in nums3:
#                 res.append(i)
#         return set(res)