class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        M =len(word2)
        N = len(word1)

        dp = [[1000] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = 0
        for i in range(N+1):
            for j in range(M + 1):
                if i == N and j == M:
                    break
                if j < M:
                    dp[i][j+1] = min(dp[i][j] + 1, dp[i][j+1])
                if i < N:
                    dp[i+1][j] = min(dp[i][j] + 1, dp[i+1][j])
                if i < N and j < M:
                    if  word1[i-1+1] == word2[j-1+1]:
                        dp[i+1][j+1] = min(dp[i][j], dp[i+1][j+1])
                    else: dp[i+1][j+1] = min(dp[i][j]+1, dp[i+1][j+1])


        return dp[N][M]


    #  이걸 내가 한게 맞나,, 발상이 엄밀한지도 생각해봐야( 발상의 구현 말고)