class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = nums.count(0)
        white = nums.count(1)
        blue = nums.count(2)
        i = 0
        while red > 0:
            nums[i] = 0
            i += 1
            red -= 1
        while white > 0:
            nums[i] = 1
            i += 1
            white -= 1
        while blue > 0:
            nums[i] = 2
            i += 1
            blue -= 1
        
                         