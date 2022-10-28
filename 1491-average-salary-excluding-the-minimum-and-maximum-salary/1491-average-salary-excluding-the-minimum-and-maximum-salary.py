class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary = salary[1:-1]
        res = 0
        for i in salary:
            res += i
        return res/len(salary)  
        