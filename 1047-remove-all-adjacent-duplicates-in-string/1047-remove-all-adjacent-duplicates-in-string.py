class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        check = []
        
        for i in s:
            if stack:
                if i != check[-1]:
                    stack.append(i) 
                    check.append(i)
                else:
                    stack.pop()
                    check.pop()
                    
            else:
                stack.append(i) 
                check.append(i)
        
        output = ''.join(stack)
        return output
        