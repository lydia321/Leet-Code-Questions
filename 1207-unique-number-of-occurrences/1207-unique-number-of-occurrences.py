class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res = Counter(arr) 
        occurrence = res.values()
        return len(occurrence) == len(set(occurrence))
        