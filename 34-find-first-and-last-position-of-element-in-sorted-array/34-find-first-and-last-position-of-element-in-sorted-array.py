class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output=[]
        res=[]
        if target not in nums:
            return [-1,-1]
        for i in range(0,len(nums)):
            if nums[i]==target:
                output.append(i)
        res.append(min(output))
        res.append(max(output))
        return res
                
       