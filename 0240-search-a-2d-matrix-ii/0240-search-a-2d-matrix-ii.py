class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for m in range(len(matrix)):
            curr = matrix[m]
            print(curr)
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
            else:
                continue
        return False