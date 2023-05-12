class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        '''
        1) Skip decision or solve it 
        2) if solved, you cant solve the next brainpower[i] questions
        
        '''
        cache = {}
        
        def dp(i):
            if i >= len(questions):
                return 0
            if i in cache:
                return cache[i]
            solve = questions[i][0] + dp(i + questions[i][1] + 1) 
            skip = dp(i + 1)
            
            cache[i] = max(solve,skip)
            return cache[i]
        
        
        return dp(0)