class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        
        while l <= r:
            m = (l+r)//2
            
            curr = matrix[m]
            left,right = 0,len(curr)-1
            if curr[left] <= target <= curr[right]:
                
                while left <= right:
                    mid = (left+right)//2
                    if curr[mid] == target:
                        return True
                    elif curr[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
                return False   
            elif curr[left] > target:
                r = m - 1
            else:
                l = m + 1
            
        return False
                
                
                
                
                
                