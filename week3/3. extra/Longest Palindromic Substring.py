class Solution:
    def longestPalindrome(self, s: str) -> str:

        # O(N^2) 이지만, 여전히 4초
        maxstr = (0,0)
        # dp[위치][본 길이]
        #  == dp[start][end] 에 palindrome 길이 저장, 
        N = len(s)

        dp = [[0]*N for _ in range(N)]

        
        for length in range(1,N+1):
            for ep in range(N):
                sp = ep - length + 1
                if sp < 0: continue

                if s[ep] == s[sp] :
                    if length == 2:
                        dp[sp][ep] = 2
                    elif length == 1: 
                        dp[sp][ep] = 1
                    elif dp[sp+1][ep-1] > 0:
                        dp[sp][ep] = dp[sp+1][ep-1] + 2
                    else: dp[sp][ep] = 0
                else: dp[sp][ep] = 0

                if dp[sp][ep] > maxstr[1] - maxstr[0] + 1:
                    maxstr = sp, ep

        
        return s[maxstr[0]: maxstr[1] + 1]

            
            


                
