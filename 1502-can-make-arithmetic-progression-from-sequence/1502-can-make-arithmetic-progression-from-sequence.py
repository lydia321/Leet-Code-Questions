class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        k = arr[1]-arr[0]
        print(k)
        for i in range(2,len(arr)):
            if arr[i]-arr[i-1] != k:
                return False
        return True    
            
             
            