class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        curr = 0   
      
        for i in range(len(flowerbed)):
            
            if flowerbed[i] == 0 and ( i-1 < 0 or flowerbed[i-1] == 0 ) and (i + 1 >= len(flowerbed) or flowerbed[i+1] == 0):
                curr += 1
                flowerbed[i] = 1 
             
            if curr >= n:
                return True
        return False