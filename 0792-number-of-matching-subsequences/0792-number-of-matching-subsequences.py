class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dict = defaultdict(list)
        for word in words:
            dict[word[0]].append(word)
        # print(dict)
        res = 0
        
        for c in s:
            curr = dict[c]
            dict[c] = []
            for each in curr:
                if len(each) == 1:
                    res += 1
                else:
                    dict[each[1]].append(each[1:])
        return res