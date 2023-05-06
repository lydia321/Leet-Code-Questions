class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        starting = ['1','2','3','4','5','6','7','8','9']
        nums = ['0','1','2','3','4','5','6','7','8','9']
        
        def dfs(curr,res):
            if int(curr) >  n:
                return res
            res.append(int(curr))
            
            for nxt in nums:
                res = dfs(curr + nxt,res)
            
            return res
            
        for each in starting:
            res = dfs(each,res)
        
        return res