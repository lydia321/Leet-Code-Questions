class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        dict = {}
        res = []
        for i in nums:
            if (i > 0 and -i in dict) or (i < 0 and abs(i) in dict):
                res.append(abs(i))
            dict[i] = 1
        # print(dict,res)
        if len(res) == 0: return -1
        return max(res)