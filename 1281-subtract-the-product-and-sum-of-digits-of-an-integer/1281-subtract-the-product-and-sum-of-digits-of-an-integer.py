class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1   
        sum_ = 0
        nn = str(n)
        for i in range(len(nn)):
            prod *= int(nn[i])
            print(prod)
            sum_ += int(nn[i])
        print(prod)
        return prod - sum_    
            
            
                
        