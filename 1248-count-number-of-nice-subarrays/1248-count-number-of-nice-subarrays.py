class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        remainders = []
        rem = 0
        res = 0
        prefix = {0: 1}
        for num in nums:
            rem += num % 2
            remainders.append(rem)
        print(remainders)
        
        for remainder in remainders:
            if remainder - k in prefix:
                res += prefix[remainder - k]
            prefix[remainder] = 1 + prefix.get(remainder, 0)
            # if remainder not in prefix:
            # 	prefix[remainder] =1
            # else:
            # 	prefix[remainder] += 1
        return res
#         N = []
#         for i in nums:
#             if i%2 == 0:
#                 N.append(0)
#             else:
#                 N.append(1)
#         print(N)
        
#         l = 0
#         res = 0
#         curr = 0
#         for r in range(len(N)): 
#             curr += N[r]
#             if curr == k:
#                 res += 1
#             while (curr - k) == 0:
#                 curr -= N[l]
#                 l += 1
           
#         return res
            