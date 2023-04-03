class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        arr = []
        for i in range(len(s) + 1):
            arr.append(i)
        # print(arr)
        l = 0
        r = len(arr) - 1
        res = []
        for i in s:
            if i == "I":
                res.append(arr[l])
                l += 1
            else:
                res.append(arr[r])
                r -= 1
        for i in arr:
            if i not in res:
                res.append(i)
        return res
            