class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half=nums[:n]
        second_half=nums[n:]
        output=[]
        for i in range(n):
            output.append(first_half[i])
            output.append(second_half[i])
        return output
            
            
            
        