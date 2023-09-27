class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = list(zip(ages,scores))
        n.sort(key=lambda x: (x[0], x[1]))

        print(n)
        dp = []
        for i in n:
            dp.append(i[1])
        
        for i in range(len(n)-1,-1,-1):
            for j in range(i+1,len(n)):
                if n[i][1] <= n[j][1]:
                    dp[i] = max(dp[i], dp[j] + n[i][1])
        # print(dp)
        return max(dp)