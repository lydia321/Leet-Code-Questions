class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lookup={}
        output=[]
        
        for i in range(len(names)):
            if names[i] not in lookup:
                lookup[heights[i]] = names[i]
            else:
                break
        heights.sort(reverse=True)
        print(lookup)
        
        for i in heights:
            for idx,val in lookup.items():
                if i == idx:
                    output.append(val)
        return output
            
        