class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        l = 0 
        
        num = str(num)
        count = 0
        
        while k <= len(num):
            curr = int(num[l:k])
            
            if not curr:
                l += 1
                k += 1

                continue
            
            if int(num) %curr == 0:
                count += 1
            l += 1
            k += 1
        return count