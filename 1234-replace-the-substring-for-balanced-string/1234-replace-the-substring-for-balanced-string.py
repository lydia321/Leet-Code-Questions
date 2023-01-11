class Solution:
    def balancedString(self, s: str) -> int:
        number_of_apperance = len(s)//4
        lookup = {}
        
        for i in range(len(s)):
            lookup[s[i]] = 1 + lookup.get(s[i],0)
        if max(lookup.values()) == number_of_apperance:
            return 0
        # print(lookup)    
        res = len(s)
        l = 0
        for r in range(len(s)):
            if s[r] in lookup: lookup[s[r]] -= 1
            while max(lookup.values()) <= number_of_apperance:
                res = min(res, r - l + 1)
                if s[l] in lookup: lookup[s[l]] += 1
                l += 1
        return res
        