class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1],reverse = True)
        # print(boxTypes)
        res = 0
        curr = truckSize
        
        for i in boxTypes:
            for j in range(i[0]):
                if curr > 0:
                    curr -= 1
                    res += i[1]
        return res
                
            
            