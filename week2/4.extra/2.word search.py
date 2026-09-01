# 맞습니다. 가능한 pruning을 전부 찾아내는 것 자체는 좋은 학습 목표가 아닙니다. 그건 결국 특정 문제의 최적화 트릭 수집에 가까워질 수 있습니다.

# 이번 문제에서 더 중요한 학습 목표는 다음 정도면 충분합니다.

# 기본 탐색이 왜 정확한지 설명할 수 있다.
# 탐색량이 왜 커지는지 설명할 수 있다.
# pruning이 필요할 때 “정답이라면 반드시 만족해야 하는 필요조건이 있는가?”라는 질문을 떠올릴 수 있다.
# 그 질문으로 문자 개수 같은 pruning 하나를 실제로 스스로 찾아냈다.
# 추가 pruning은 구현 비용 대비 효과가 있는지 판단한다.

# 즉 목표는

# 모든 pruning을 발견한다

# 가 아니라

# 탐색이 비싸다고 판단했을 때 pruning 후보를 찾는 사고 절차를 가지고 있다

# 에 가깝습니다.

# 실전에서도 stopping criterion이 필요합니다. 기본 풀이가 제한을 충분히 통과할 것으로 예상된다면 더 복잡한 pruning을 계속 찾을 이유가 없습니다. 반대로 시간 제한이 빡빡하거나 실제로 TLE가 난다면 그때 다음 pruning을 검토하면 됩니다.

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in board]


        def recursive_find(wordidx, pos):
            y, x = pos
            if word[wordidx] == board[y][x]:
                if wordidx == len(word) - 1:
                    return True
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or visited[ny][nx]:
                        continue
                    else:
                        visited[ny][nx] = True
                        res = recursive_find(wordidx+1, (ny, nx))
                        visited[ny][nx] = False
                        if res:
                            return True

            else: return False
                
        #  pruning에 대해, word와 table간의 필요조건에 대해 고려할 필요 있다.
        #  애초에 찾을 수 없는 조건을 생각해보기 -> 특정 문자의 개수가 board에서의 총 개수보다 많다면, 못 찾는다. N * M 시간만에 찾으므로, recursive 보다 절약한다.

        '''
        현재 독립적으로 가져갈 지점은 당신이 직접 찾아낸 이것입니다.

탐색 중 가지치기만 보지 말고, 탐색 전에 전체 입력이 정답의 필요조건을 충족하는지도 검사할 수 있다.

여기서 다음 사고 과제는 하나뿐입니다.

새로운 pruning을 찾으려고 할 때, “무엇을 더 검사할까?”가 아니라 “정답이 존재한다면 반드시 참이어야 하는 조건이 또 무엇인가?”라고 질문해보세요.
        '''


        for i in range(n):
            for j in range(m):
                visited[i][j] = True
                if recursive_find(0, (i, j)): return True
                visited[i][j] = False

        return False
