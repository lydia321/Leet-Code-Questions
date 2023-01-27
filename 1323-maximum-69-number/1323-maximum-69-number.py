class Solution:
    def maximum69Number (self, num: int) -> int:
        res = list(str(num))
        print(res)
        for i,val in enumerate(res):
            if val == '6':
                res[i] = '9'
                break
        return int(''.join(res))
                
            