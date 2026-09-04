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
    in_degrees = defaultdict(set)  # edge 중복 무시
    # TODO: 그래프 구성 및 진입 차수 계산
    pass
    for vertex in range(vertices):     # in-degrees만 사용하기 때문에, 들어오는 edge가 없는 vertices도 len() 위해 생성해줘야 함/
        in_degrees[vertex] = set()

    for f, t in edges:
        in_degrees[t].add(f)
    # TODO: 진입 차수가 0인 정점들을 큐에 추가
    pass
    q = deque([k  for k, v in in_degrees.items() if len(v) == 0])
    result = []
    
    # TODO: 큐가 빌 때까지 반복  -> 연결되어 있는 것들만 가능?
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들의 진입 차수 감소
    pass
    while q:
        cur_v = q.pop()
        result.append(cur_v)
        for k, v in edges:   # graph 구현 없어서 edge 순회 -> 중복이 그대로 반영됨 :(
            if k == cur_v:
                if in_degrees[v]:
                    in_degrees[v].remove(k)

                if not in_degrees[v]: # falsy하면
                    q.appendleft(v)

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
