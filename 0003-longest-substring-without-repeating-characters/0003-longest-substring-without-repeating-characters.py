class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = deque()
        res = 0
     
        for r in s:
            while r in lookup:
                lookup.popleft()
            lookup.append(r)
            res = max(res,len(lookup))
        return res