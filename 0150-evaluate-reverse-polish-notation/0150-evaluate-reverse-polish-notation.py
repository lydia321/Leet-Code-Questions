class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = ['*','-','+','/']
        
        for i in tokens:
            if i not in operand:
                stack.append(i)
                
            elif i == '+':
                sum_ = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(sum_)  
                    
            elif i == '-':
                diff = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(diff)  
            elif i == '*':
                mul = int(stack[-1])*int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(mul)
            elif i == '/':
                div =(int(float(int(stack[-2]))/int(stack[-1])))
                stack.pop()
                stack.pop()
                stack.append(div)
        return stack[0]      
                
                
            