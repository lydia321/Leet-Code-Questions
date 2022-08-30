class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        evenArr = []
        oddArr = []
        for i in nums:
            if i % 2 == 0:
                evenArr.append(i)
            else:
                oddArr.append(i)
        for i in range(len(evenArr)):
            output.append(evenArr[i])
            output.append(oddArr[i])
        return output
    
                