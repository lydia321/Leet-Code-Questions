class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
                
#         arr = []  
        
#         for i in range(len(temp)-1):
#             for j in range(i+1,len(temp)):
#                 if temp[i]<temp[j]:
#                     j-i
#                     arr.append(j-i)    
#                     break  
#             else:
#                 arr.append(0)
#         arr.append(0)
#         return arr  
        stack = []   
        res = [0]*len(temp)
    
        for i in range(len(temp)):
            while stack and temp[i]>temp[stack[-1]]:
                diff = i-stack[-1]
                print(diff)
                res[stack[-1]] = diff
                stack.pop()  
                temp[i]
            stack.append(i)    
        return res    
        
                