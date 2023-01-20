class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        a,b=0,0
        
        while a < len(nums1) and b < len(nums2):
            if nums1[a] < nums2[b]:
                res.append(nums1[a])
                a += 1
            else:
                res.append(nums2[b])
                b += 1
        while a < len(nums1):
            res.append(nums1[a])
            a += 1
        while b < len(nums2):
            res.append(nums2[b])
            b += 1
        print(res)
        m = len(res)//2
        if len(res)%2 == 0:
            return (res[m] + res[m-1])/2
        
        return res[m]
                