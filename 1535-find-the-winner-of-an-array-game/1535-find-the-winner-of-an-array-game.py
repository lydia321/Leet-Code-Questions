class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        remaining_round = 0
        winner = -1
        curr_winner = -1
        if k >= len(arr):
            return max(arr)
        while remaining_round < k:
           
            if arr[0] > arr[1]:
                ma = arr.pop(1)
                arr.append(ma)
             
            else:
                ma = arr.pop(0)
                arr.append(ma)
          
           
            curr_winner = arr[0]
            if curr_winner != winner:
                winner = curr_winner
                remaining_round = 1
            else:
                remaining_round += 1
        return winner
            
            