class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse= True)
        arr=nums[:2]
        arr=(arr[0]-1)*(arr[1]-1)
        return arr