class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.dict = defaultdict(int)
        
        for i in self.nums2:
            self.dict[i] += 1
        
        
    def add(self, index: int, val: int) -> None:       
        self.dict[self.nums2[index]] -= 1
        self.dict[self.nums2[index] + val] += 1 
        self.nums2[index] += val
        

        
    def count(self, tot: int) -> int:
          
        count = 0
        for i in self.nums1:
            curr = tot - i
            count += self.dict[curr]
        return count
            


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
