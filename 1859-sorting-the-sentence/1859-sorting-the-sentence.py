class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s =s.split()
        
        word={}
        output=''
        for i in s:
            word[i[-1]]=i[:-1]
            
        for i in sorted(word):
            output=output+''.join(word[i])+' '
        output=output[:-1]
        
        return output