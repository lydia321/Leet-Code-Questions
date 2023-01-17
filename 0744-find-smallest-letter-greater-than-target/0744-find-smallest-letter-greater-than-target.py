class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = letters[0]
        
        for i in letters:
            if ord(i) > ord(target):
                return i
        return res
        