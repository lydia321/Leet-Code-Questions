class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ''
        
        for i in address:
            if i != '.':
                res = res + i
            else:
                res = res + '[' + i + ']'
        return res
                
        