class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0 
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1):
                subArr = arr[i:j]
                if len(subArr)%2 ==1:
                    res += sum(subArr)
        return res   
           
        
     