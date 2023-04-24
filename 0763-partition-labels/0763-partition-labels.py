class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict = defaultdict(list)
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]][1] = i
            else: dict[s[i]] = [i,i]
        # print(dict)
        res = []
     
        for i,val in dict.items():
            if res and res[-1][0] < val[0] and res[-1][1] > val[1]:
                continue
            else:
                res.append(val)
        # print(res)
        final = []
        for i in range(len(res)):
            if final and ((final[-1][0] < res[i][0] < final[-1][1]) or (final[-1][0] < res[i][1] < final[-1][1])):
                val = [min(final[-1][0],res[i][0]), max(final[-1][1], res[i][1])]
                final.pop()
                final.append(val)
            else:
                final.append(res[i])
        # print(final)
        a = []
        for i in final:
            a.append(i[1] - i[0] + 1)
        return a