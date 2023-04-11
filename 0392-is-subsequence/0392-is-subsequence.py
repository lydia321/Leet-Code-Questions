class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = len(s) - 1
        t_ptr = len(t) - 1
        
        while s_ptr >= 0 and t_ptr >= 0:
            if s[s_ptr] == t[t_ptr]:
                print(s[s_ptr])
                s_ptr -= 1
                t_ptr -= 1
            else:
                t_ptr -= 1
        return s_ptr == -1
        