class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        res = inf
        n = set(nums1)
        n2 = set(nums2)
        for i in n:
            if i in n2 and i < res:
                res = i
        return res if res != inf else -1