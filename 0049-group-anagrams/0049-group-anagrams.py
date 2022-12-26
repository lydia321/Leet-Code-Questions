class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        
        for i in strs:
            curr = ''.join(sorted(i))
           
            if curr in dict:
                dict[curr].append(i)   
            else:
                dict[curr] = [i]
        print(dict)
        return dict.values()
    