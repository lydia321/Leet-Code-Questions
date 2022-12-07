class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        curr = strs[0]
        
        for i in range(len(curr)):
            for j in range(1,len(strs)):
                if i > len(strs[j])-1 or curr[i] != strs[j][i]:
                    return res
            res += curr[i]
        return res
                
            
            
            
        