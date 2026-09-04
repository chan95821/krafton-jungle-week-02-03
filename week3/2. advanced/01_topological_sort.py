"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque, defaultdict
def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # TODO: 그래프와 진입 차수 초기화
    pass
    in_degrees = [0] * vertices
    graph = [set() for _ in range(vertices)]
    for f, t in edges:
        graph[f].add(t)
    for f in graph:
        for t in f:
            in_degrees[t] += 1

    # TODO: 진입 차수가 0인 정점들을 큐에 추가

    pass
    q = deque([vertex for vertex, cnt in enumerate(in_degrees) if cnt == 0])
    result = []
    
    # TODO: 큐가 빌 때까지 반복  -> 연결되어 있는 것들만 가능?
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들의 진입 차수 감소
    
    while q:
        vertex_from = q.pop()
        result.append(vertex_from)   
        for vertex_to in graph[vertex_from]:
            in_degrees[vertex_to] -= 1
            if in_degrees[vertex_to] == 0:
                q.appendleft(vertex_to)
        in_degrees[vertex_from] = -1 # 다시 방문하지 않게 -1 처리

        # q += [v for v, cnt in enumerate(in_degrees) if cnt == 0 and v in graph[vertex_from]]  # 순회 후 in degrees가 0이면 방문 가능하다 - q에 추가 , += 와 extend() 동작 같다 

    # 만약 result 개수가 vertices 개수보다 작다면, in_degrees가 0이 아닌 원소가 있는 것 <- 고립된 원소도 in_degrees가 0이니 추가된다. cycle은 항상 1 이상일 수 밖에 없으므로 result에 추가 안된다 - cyclic 부분 있다
    if len(result) < vertices: 
        return []

    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
