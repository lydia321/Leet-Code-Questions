class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        members = Counter(senate)
        skips = {'R': 0, 'D': 0}

        while queue:
            senator = queue.popleft()
            rival = ['R', 'D'][int(senator == 'R')]

            if skips[senator] > 0:
                skips[senator] -= 1
            else:
                skips[rival] += 1 
                members[rival] -= 1 
                queue.append(senator) 
            if members[rival] <= 0:
                return 'Radiant' if senator == 'R' else 'Dire'
