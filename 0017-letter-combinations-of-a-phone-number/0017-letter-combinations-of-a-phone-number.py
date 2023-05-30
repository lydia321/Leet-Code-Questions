class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': 
            return []
        lookup = {'2':["a","b","c"], '3':["d","e","f"], '4':["g","h","i"],
              '5':["j","k","l"], '6':["m","n","o"], '7':["p","q","r", "s"],
              '8':["t","u","v"], '9':["w","x","y","z"]}
        
        res = []
        def backtrack(curr, next_digits):
            if not next_digits:
                res.append(curr)
                return
            
            for each in lookup[next_digits[0]]:
                backtrack(curr + each, next_digits[1:])
        
        backtrack("", digits)
        return res
            
