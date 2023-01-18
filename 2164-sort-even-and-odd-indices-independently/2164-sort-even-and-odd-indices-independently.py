class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        arrE = []
        arrO = []
        
        for i in range(len(nums)):
            if i%2 == 0:
                arrE.append(nums[i])
            else:
                arrO.append(nums[i])
        arrE.sort(reverse = True)
        arrO.sort()
        
        res = []
        for i in range(len(nums)):
            if i%2 == 0:
                res.append(arrE[-1])
                arrE.pop()
            else:
                res.append(arrO[-1])
                arrO.pop()
        return res
    