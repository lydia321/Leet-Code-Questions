class Solution:
    def intToRoman(self, num: int) -> str:
        lookup = {1000: "M",
                  900: "CM", #special case
                  500: "D",
                  400: "CD", #special case
                  100: "C",
                  90: "XC", #special case
                  50: "L",
                  40: "XL", #special case
                  10: "X", 
                  9: "IX", #special case
                  5: "V", 
                  4:"IV", #special case
                  1:"I"
                 }
        res = ""
        
        for val in lookup:
            curr = num//val
            if curr > 0:
                res += (lookup[val])*curr
                num = num%val
        return res
