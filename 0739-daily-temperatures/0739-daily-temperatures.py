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
    
        for i,t in enumerate(temp):
            while stack and stack[-1][0] < temp[i]:
                stackt,stackidx = stack.pop()
                res[stackidx] = i-stackidx
        
            stack.append([t,i])    
        return res    