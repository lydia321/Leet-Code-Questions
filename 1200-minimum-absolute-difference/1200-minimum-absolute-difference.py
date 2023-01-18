class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        Min_Diff = float('inf')
        arr.sort()
        for i in range(len(arr)-1):
            Min_Diff = min(Min_Diff,abs(arr[i]-arr[i+1]))
        res = []
        for i in range(len(arr)-1):
            if abs(arr[i] - arr[i+1]) == Min_Diff:
                res.append([arr[i],arr[i+1]])
            
        return res