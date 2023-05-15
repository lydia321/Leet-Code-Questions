class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        
        for i in range(len(boxes)):
            curr = 0
            for j in range(len(boxes)):
                if i != j and boxes[j] == '1':
                    curr += abs(j - i)
            res.append(curr)
        return res