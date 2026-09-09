class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        M = len(matrix[0])
        drawable_sq = [[0] * (M) for _ in range(N) ]
        res = 0
        for i in range(0, N):
            for j in range(0, M):
                if i == 0 or j == 0:
                    drawable_sq[i][j] = 1 if matrix[i][j] == '1' else 0
                elif matrix[i][j] == '1':
                    drawable_sq[i][j] = min(drawable_sq[i-1][j-1] , drawable_sq[i][j-1], drawable_sq[i-1][j]) + 1
                else: drawable_sq[i][j] = 0

                res = max(res, drawable_sq[i][j])

                
        return res
            
            