class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output=[]
        i=0
        for i in range(len(arr)):
            #finding max number
            max_number=max(arr[:len(arr)-i]) 
            #finding the index of max number
            max_number_index=arr.index(max_number)+1
            #Move the maximum array to index 0
            arr[:max_number_index]=reversed(arr[:max_number_index])
            #add maximum value to output
            output.append(max_number_index)
            #Reverse the entire unsorted array
            arr[:len(arr)-i]=reversed(arr[:len(arr)-i])
            output.append(len(arr)-i)
        return output    
            