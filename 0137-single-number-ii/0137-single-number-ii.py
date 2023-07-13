class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = Counter(nums)
        # print(dict)
        
        for i,count in dict.items():
            if count == 1:
                return i
        