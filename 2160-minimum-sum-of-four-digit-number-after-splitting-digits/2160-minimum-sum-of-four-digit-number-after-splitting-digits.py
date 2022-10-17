class Solution:
    def minimumSum(self, num: int) -> int:
        output = sorted(str(num), reverse =True)
        num1 = int(output[3] + output[1]) 
        num2 = int(output[2] + output[0])
        return num1 + num2
        