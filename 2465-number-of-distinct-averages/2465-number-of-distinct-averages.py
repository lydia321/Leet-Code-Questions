class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        Avg = {}
        
        while len(nums) > 0:
            A , B = max(nums), min(nums)
            curr = ((A + B)/2)
            Avg[curr] = 1 + Avg.get(curr, 0)
            nums.pop(nums.index(A))
            nums.pop(nums.index(B))
        
        return len(Avg)