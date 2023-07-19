class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output=[]
        output2=[]
        for i,val in enumerate(points):
            res=(val[0]**2)+(val[1]**2)
          
            output.append((res,i))   
            
        output.sort()
     
        output=output[:k]
        
        for i in output:
            print(i)
            output2.append(points[i[1]])# meaning from our points we want this i's value
        return output2    
        
  