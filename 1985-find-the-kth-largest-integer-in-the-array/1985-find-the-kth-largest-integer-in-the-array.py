class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr=[]
        for i in nums:
            arr.append(int(i))
        arr.sort(reverse=True)   
        idx= str(arr[k-1]) 
        return idx
       