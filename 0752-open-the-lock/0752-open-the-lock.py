class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        visited = set(deadends)
        
        def children(lock):
            res = []
            for i in range(0,4):
                num = (int(lock[i]) + 1)%10
                digit = lock[:i] + str(num) + lock[i+1:]
                res.append(digit)
                
                num = (int(lock[i]) - 1 + 10)%10
                digit = lock[:i] + str(num) + lock[i+1:]
                res.append(digit)
                
            return res    
        queue = [('0000', 0)]
        while queue:
            curr_lock,curr_turn = queue.pop(0)
            if curr_lock == target:
                return curr_turn
            for child_lock in children(curr_lock):
                if child_lock not in visited:
                    visited.add(child_lock)
                    queue.append([child_lock,curr_turn + 1])
                    
        return -1
            