class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res = Counter(arr) 
        occurrence = res.values()
        S = set(occurrence)
        print(occurrence,S)
        return len(occurrence) == len(S)
        