class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(left,right,curr,valid):
            if left == right == 0:
                res.append(curr)
                return
            if left > 0:
                dfs(left - 1,right,curr + '(',valid + 1)
            if right > 0 and valid > 0:
                dfs(left,right - 1,curr + ')', valid - 1)
        dfs(n,n,'',0)
        return res