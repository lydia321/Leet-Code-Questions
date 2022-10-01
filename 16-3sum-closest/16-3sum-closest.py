class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        Min = float(inf)
        total = 0
        nums.sort()
        
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                sum_= nums[i] + nums[l] + nums[r]
                diff = abs(sum_ - target)
                if Min > diff:
                    Min = diff
                    total = sum_
                if sum_ > target:
                    r-=1
                elif sum_ < target:
                    l+=1
                else: return sum_
             
        return total