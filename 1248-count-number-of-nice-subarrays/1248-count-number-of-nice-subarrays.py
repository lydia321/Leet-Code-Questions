class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        stack ,Map = [] , {0:1}
        curr = res = 0
       
        for num in nums:
            curr += num % 2
            stack.append(curr)
        print(stack)
        
        for i in stack: 
            Map[i] = 1 + Map.get(i, 0)
            if i - k in Map:
                res += Map[i - k]
        return res
