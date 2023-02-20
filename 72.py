class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        dp = [[0] * (1 + len(word1)) for _ in range(1 + len(word2))]

        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue

                if word1[j-1] != word2[i-1]:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = dp[i-1][j-1]

        return dp[-1][-1]
