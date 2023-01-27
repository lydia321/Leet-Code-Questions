class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        #hint number 3
        S = []
        for i in nums:
            if i not in S and i != 0:
                S.append(i)
        return len(S)
            
            
            
        
        