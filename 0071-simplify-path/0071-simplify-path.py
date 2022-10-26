class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        stack = []
        print(arr)
        for i in arr:
            if i =="..":
                if stack:
                    stack.pop()
                else:
                    continue
            elif i == '.' or i =='':
                continue
            else:
                   
                stack.append(i)
        print(stack)
        if stack and stack[-1] == '':
            stack.pop()
        return '/'+"/".join(stack)
        
                
        