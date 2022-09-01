class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=sorted(s)
        t=sorted(t)
        answer=bool(1) 
    
        if s==t:
            return answer
        else:
            answer=bool(0)
            return answer