class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        count = 0
        for i in operations:
            if i == 'C':
                k = record.pop()
                count -= int(k)
            elif i == 'D':
                val = int(record[-1])*2
                record.append(val)
                count += val
            elif i == '+':
                sum_ = int(record[-1]) + int(record[-2])
                record.append(sum_)
                count += sum_
            else:
                record.append(i)
                count += int(i)
                    
        return count          