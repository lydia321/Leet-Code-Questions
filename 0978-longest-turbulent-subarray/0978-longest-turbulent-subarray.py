class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        
        if len(arr) == 1: return 1
        while r < len(arr):
            while r < len(arr)-1 and (arr[r-1] > arr[r] < arr[r+1] or arr[r-1] < arr[r] > arr[r+1]):
                r += 1 
            while l < r and arr[l] == arr[l+1]:
                l += 1
            res = max(res, r - l + 1)
            l = r
            r += 1
        return res
                