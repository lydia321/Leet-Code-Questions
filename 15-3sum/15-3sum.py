class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            if len(nums) < 3:
                return []
            nums.sort()
            output = set()
            for i in range(0,len(nums)):
                l = 1 + i
                r = len(nums)-1
                val=nums[i]
                
                while l < r:
                    s = val + nums[l] + nums[r]
                    if s == 0:
                        output.add((val,nums[l],nums[r]))
                        r-= 1
                        l+= 1
                    elif s > 0:
                        r-= 1
                    else:
                        l+= 1
            return output             
                    
           