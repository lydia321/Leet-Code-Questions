class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        1) Ignore white spaces
        2) if next value is any other char other than int return
        3) no leading zeros
        '''
        start = True
        res = ''
        nums = '0123456789'
        sign = '-+'
        neg = False
        maxInt, minInt = 2**31 - 1 , -2**31
        for i in s:
            if start and i in sign:
                if i == '-': neg = True
                start = False
            elif (start and i == '0') :
                start = False
                continue
            elif start and i == ' ':
                continue
            elif start and i != '0' and i in nums:
                start = False
                res += i
            elif i in nums:
                res += i
            else:
                break
        print(res)
        
        if len(res) == 0 or (len(res) == 1 and res[0] == '-' ): 
            return 0
        if neg:
            res = -int(res)
        else: res = int(res)
        res = max(res, -2**31)
        res = min(res, (2**31)-1)
        return res
       