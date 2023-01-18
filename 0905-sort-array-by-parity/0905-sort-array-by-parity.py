class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arrL= []
        arrR = []
        
        for i in nums:
            if i%2==0:
                arrL.append(i)
            else:
                arrR.append(i)
        arrL.extend(arrR)
        return arrL