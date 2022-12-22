class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res = ''
        
        for i in title.split():
            if len(i) < 3:
                curr = i.lower()
                res += curr
                res += ' '
            else:
                
                a = i[0].upper()
                b = i[1:].lower()
                res += a
                res += b
                res += ' '
        return res[:-1]
                