class Solution(object):
    def minCut(self, s):
        n = len(s)

        dp = [0] * n

        for i in range(n):
            dp[i] = i

            for j in range(i + 1):
                sub = s[j:i + 1]

                if sub == sub[::-1]:
                    if j == 0:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[n - 1]
        