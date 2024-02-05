class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dfs(i,left):
            if i == len(s):
                if left == 0:
                    return True
                else:
                    return False
            
            if s[i] == "(":
                return dfs(i+1,left + 1)
            elif s[i] == ")":
                if left > 0:
                    return dfs(i+1,left - 1 )
                else:
                    return  False
            else:
                res = dfs(i + 1, left + 1 )
                if res:
                    return True
                if left > 0:
                    res = res or (dfs(i + 1, left- 1))
                
                res = res or (dfs(i + 1, left) )
            return res 
        return dfs(0,0)
      
    