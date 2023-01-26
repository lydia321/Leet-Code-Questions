class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                val = (-(nums1[i]+nums2[j]),[nums1[i],nums2[j]])
                if len(heap) < k:
                    heapq.heappush(heap,(val))
                # print(heap)
                else:
                    if(nums1[i]+nums2[j]) > -heap[0][0]:
                        break
                    else:
                        heapq.heappop(heap)
                        heapq.heappush(heap,(val))
        # print(heap)
        res = []
        for i in heap:
            res.append(i[1])
        # print(res)
        return res
                    
        
    
        