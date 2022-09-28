class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        output=[]
        for i in arr2:
            if i in arr1:
                a=arr1.count(i)
                for j in range(a):
                    output.append(i)
                    arr1.remove(i)
        return output + sorted(arr1)            