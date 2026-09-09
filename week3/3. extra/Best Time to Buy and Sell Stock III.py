class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-10000]*(len(prices) + 1) for _ in range(5)]

        for idx in range(len(prices) + 1):
            dp[0][idx] = 0
        
        for transaction in range(5):
            for prev_idx in range(transaction, len(prices)):
                # 각 날짜에 대해 단방향 흘러가므로, 같은 날짜라면 이익이 가장 큰 것이 항상 유리하다 -> 선택 문제, greedy, 
                #  그 transaction 안하는 경우 - 하는 경우와 시간이 다른데, 과거가 먼저 최대로 되어야 이후가 최대 보장된다
                dp[transaction][prev_idx+1] = max(dp[transaction][prev_idx+1], dp[transaction][prev_idx])

                if transaction < 4:  # 사거나 팔 수 있다
                    if transaction % 2 == 0: # 사는 경우
                        cur_balance = dp[transaction][prev_idx] - prices[prev_idx-1 + 1]
                    else: #파는 경우
                        cur_balance = dp[transaction][prev_idx] + prices[prev_idx -1 +1]
                    dp[transaction + 1][prev_idx + 1] = max(dp[transaction+1][prev_idx+1], cur_balance)
                               


        return max(dp[0]+ dp[2]+ dp[4])

