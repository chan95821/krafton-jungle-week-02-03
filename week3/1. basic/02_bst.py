"""
[이진 검색 트리 - Binary Search Tree (BST)]

문제 설명:
- 이진 검색 트리에서 값을 검색합니다.
- BST 특징: 왼쪽 자식 < 부모 < 오른쪽 자식
- 이 특성을 이용하여 빠른 검색이 가능합니다.
- 왼쪽 서브트리의 모든 값 < 현재 노드 값
- 오른쪽 서브트리의 모든 값 > 현재 노드 값

입력:
- root: 트리의 루트 노드
- target: 찾을 값

출력:
- True: 값이 존재
- False: 값이 없음

예제:
트리:
      5
     / \
    3   7     # 자식 트리의 모든 원소가
   / \
  2   4

찾는 값: 4 → True
찾는 값: 6 → False

힌트:
- target < root.value → 왼쪽으로 이동
- target > root.value → 오른쪽으로 이동
- target == root.value → 찾음!
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left : TreeNode | None = None #Type Hinting은 사용되지는 않지만 __annotations__에 저장하기 때문에, Pydantic이 type 확인할 수 있다
        self.right: TreeNode | None = None

def search_bst(root, target):
    """
    BST에서 값 검색
    
    Args:
        root: 트리 루트
        target: 찾을 값
    
    Returns:
        True/False
    """
    # TODO: root가 None이면 False 반환
    
    if root is None: # 여담 : python equality(==) 는 보통 nested item을 모두 비교한다. \
        # 그렇지만 dunder로 __eq__ 구현해야 하므로, 기본 행동은 아니다. 정의 없으면 Object Identity만 비교한다.
        return False
    # TODO: 값을 찾으면 True 반환
    node = root
    while node is not None:
        if node.value == target:
            return True
        elif node.value > target:
            node = node.left
        elif node.value < target:
            node = node.right
    return False


# 테스트 케이스
if __name__ == "__main__":
    # BST 생성:
    #       5
    #      / \
    #     3   7
    #    / \
    #   2   4
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    
    print("=== 이진 검색 트리 ===")
    print("트리 구조: 5를 루트로 하는 BST")
    
    test_values = [2, 4, 5, 6, 7]
    for val in test_values:
        result = search_bst(root, val)
        print(f"값 {val} 검색: {result}")


