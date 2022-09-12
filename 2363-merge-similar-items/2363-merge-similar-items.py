class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        output=[]
        for item1 in items1:
            for item2 in items2:
                if item1[0]==item2[0]:
                    item1[1]=item1[1]+item2[1]
                    items2.remove(item2)
        return sorted(items1+items2)            
                    
        