class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        arr = Counter(nums)
        # print(arr)
        res = []
        count = max(arr.values())
        
        while count > 0:
            count -= 1
            curr = []
            for each in arr:
                if arr[each] > 0:
                    curr.append(each)
                    arr[each] -= 1
            
            res.append(curr)
        return res
                