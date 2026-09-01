"""
[해시 테이블 - 학생 성적 관리]

참고:
- 파이썬의 딕셔너리(dict)는 내부적으로 해시 테이블로 구현되어 있습니다.
- 따라서 딕셔너리를 사용하면 해시 테이블의 특성을 그대로 활용할 수 있습니다.
- week1의 01번 문제를 복기 해 보세요.

문제 설명:
- 해시 테이블(딕셔너리)을 사용하여 학생 성적을 관리합니다.
- Key-Value 쌍으로 빠른 검색, 삽입, 삭제가 가능합니다.

입력:
- 학생 이름과 점수

출력:
- 평균 점수
- 최고 점수 학생
- 특정 학생 점수 조회

예제:
입력: {"Alice": 85, "Bob": 92, "Charlie": 78}
출력:
평균 점수: 85.0
최고 점수: Bob (92점)

힌트:
- 딕셔너리 사용
- 평균: sum(scores.values()) / len(scores)
- 최고점: max(scores, key=scores.get)
"""
from builtins import hash
from math import inf
class Node:
    """
    연결 리스트의 노드 (한 칸 = 데이터 + 다음 화살표)

        ┌──────┬──────┐
        │ data │ next │ ──▶ (다른 Node 또는 None)
        └──────┴──────┘
    """
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None #pylance용 type hinting

class LinkedList:
    """
    단순 연결 리스트 (Singly Linked List)

        head ──▶ [data|next] ──▶ [data|next] ──▶ ... ──▶ [data|None]
    """
    def __init__(self):
        self.head = None 

    def append(self, data):
        """
        리스트 끝에 노드 추가

        그림으로 보는 두 가지 경우:

        ① 비어 있을 때 (self.head is None)
              head ─▶ None     ──append(7)──▶    head ─▶ [7|None]

        ② 이미 노드가 있을 때
              head ─▶ [1|●]─▶[2|None]
                                       ──append(7)──▶
              head ─▶ [1|●]─▶[2|●]─▶[7|None]
        """
        new_node = Node(data)

        # ─── Level 1: 리스트가 비어 있는 경우 ────────────────────────
        if self.head is None:
            self.head = new_node
            return
        # 새 노드를 앞에 붙이고 끝내기  O(1)
        tobesecond = self.head
        self.head = new_node
        new_node.next = tobesecond

    def remove(self, data):
        pass
    
    



class HashTable:
    max_keyval = 20
    def __init__(self):
        self.table = [LinkedList()] * self.max_keyval

    def insert(self, item):
        list = self.table[hash(item[0]) % self.max_keyval]
        list.append(item)

    def find(self, key):
        list = self.table[hash(key) % self.max_keyval]
        if list.head is None:
            return None
        else:
            node = list.head
            while node is not None:
                if node.data[0] == key:
                    return node.data[1]
                else:
                    node = node.next
            return None






def manage_grades(students):
    """
    학생 성적 관리 시스템
    
    Args:
        students: {이름: 점수} 딕셔너리
    
    Returns:
        평균, 최고점 학생 이름, 최고점
    """
    # TODO: 평균 점수 계산
    pass
    score_sum = 0
    top_score = -1
    for name, score in students.items():
        score_sum += score
        if top_score < score:    # 동일 점수 존재시 list 고려, 기대  출력에 list 표현 없어서 단독 최고 점수만 고려
            top_student = name
            top_score = score

    average = score_sum / len(students)
        
    # TODO: 최고 점수 학생 찾기
    pass
    
    return average, top_student, top_score

def find_student_score(students:HashTable, name:str):
    """
    특정 학생의 점수 조회
    
    Args:
        students: 학생 딕셔너리
        name: 찾을 학생 이름
    
    Returns:
        점수 (없으면 None)
    """
    # TODO: students에서 name 찾기
    return students.get(name) #예외 발생 말고 None 반환, 아니면 in 사용하기

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    students1 = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95
    }
    students1 = HashTable()
    
    print("=== 학생 성적 관리 ===")
    avg, top_name, top_score = manage_grades(students1)
    print(f"평균 점수: {avg}")
    print(f"최고 점수: {top_name} ({top_score}점)")
    print()
    
    # 테스트 케이스 2: 학생 조회
    print("=== 학생 점수 조회 ===")
    search_name = "Alice"
    score = find_student_score(students1, search_name)
    print(f"{search_name}의 점수: {score}")
    print()
    
    search_name2 = "Eve"
    score2 = find_student_score(students1, search_name2)
    print(f"{search_name2}의 점수: {score2}")


