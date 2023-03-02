class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        fewest_coin = 1
        visited_coins = set(coins)
        queue = deque(coins)
        
        while queue:
            for _ in range(len(queue)):
                curr_coin = queue.popleft()
                if amount == curr_coin:
                    return fewest_coin
                
                for each in coins:
                    possible_coin = curr_coin + each
                    if possible_coin not in visited_coins and possible_coin <= amount:
                        visited_coins.add(possible_coin)
                        queue.append(possible_coin)
            fewest_coin += 1
        return -1