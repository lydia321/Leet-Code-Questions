class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = count = 0
        currSum = sum(arr[l:k])
       
        if (currSum//k) >= threshold:    count += 1
    
        for r in range(k,len(arr)):
            currSum -= arr[l] 
            currSum += arr[r]
            
            if (currSum//k) >= threshold:    count += 1
            
            l += 1
        return count
            
        