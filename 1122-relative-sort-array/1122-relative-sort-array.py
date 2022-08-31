import numpy as np
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        output=[]
        for i in arr2:
            if i in arr1:
                for j in range(arr1.count(i)):
                    output.append(i)
                    arr1.remove(i)
        return output + sorted(arr1)        
                       
                       
                      
        