class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            dict[i] = 1 + dict.get(i,0)
        # print(dict)
        
        dictlist = defaultdict(list)
        for i in dict:
            dictlist[dict[i]].append(i)
        
        res = []
        # print(dictlist)
        for freq,list_ in sorted(dictlist.items(),reverse = True):
            for num in list_:
                res.append(num)
                if len(res) == k:
                    return res
        
        
        