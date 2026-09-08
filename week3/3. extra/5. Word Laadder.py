from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bruteforce 비교시 WORD^2 * wordlength/ wordlength서로 다른 경우 생각해봐야 
        # BFS는 O(V + E) E는 최악 V^2
        # TODO: wildcard 방법 써봐야 

        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        graph = {k : [] for k in wordList}

        for i, str_i in enumerate(wordList):
            for j in range(i+1, len(wordList)):
                str_j = wordList[j]
                diff = 0
                if len(str_i) != len(str_j):
                    continue
                for ch_idx, ch_i in enumerate(str_i): # <= wordLength            
                    if ch_i != str_j[ch_idx]:
                        diff += 1
                
                if diff == 1:
                    graph[str_i].append(str_j)
                    graph[str_j].append(str_i)

        #  bfs 로 최단 거리 탐색

        visited = {}
        visited[beginWord] = 1
        q = deque([beginWord])

        while q:
            from_v = q.pop()
            for to_v in graph[from_v]:
                if visited.get(to_v, 9999) > visited[from_v] + 1: # 현재 로직은 비교를 염두에 뒀지만, 가중치가 같으므로, 먼저 발견했으면 가장 최선이다. 그러니 방문 안했는지만 알면 된다. 
                    visited[to_v] = visited[from_v] + 1
                    q.appendleft(to_v)

        return visited[endWord] if visited.get(endWord) else 0
                    


        #  graph가 dict이니, beginword가 있는지는 마지막에 비교하자