class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        paper = 0
        glass = 0
        metal = 0
        t = [0]
        for i in travel: t.append(i)
        
        end = {}
        for i in range(len(garbage)):
            for each in garbage[i]:
                end[each] = i
        print(end)
        for i in range(len(garbage)):
            for each in garbage[i]:
                if each == "P":
                    paper += 1
                   
                elif each == "M":
                    metal += 1
                
                else:
                    print(glass)
                    glass += 1
            if 'G' in end and i <= end["G"]:
                glass += t[i]
            if 'P' in end and i <= end["P"]:
                paper += t[i]
            if "M" in end and i <= end["M"]:
                metal += t[i]
        # print(paper,glass,metal)
        return paper + glass + metal
            
                
                
     
                
                