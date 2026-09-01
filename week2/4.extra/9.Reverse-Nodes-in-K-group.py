# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #각 묶음에 대해 : 묶음을 먼저 나누기. 만약 그 다음이 수가 적다면 그대로 끝내기

            #1.각 묶음에서 : 끝 노드부터 시작해 시작 노드까지 순서 바꾼 새 리스트 만들기
        #해당 묶음을 새로 연결하기

            #2. 각 묶음에서 : 양쪽 끝, 끝의 외부 노드 기억하고, 나머지에 대해 가리키는 방향만 바꾸기. 이후 양 쪽 끝을 해당 외부노드로 바꾸어 링크하기
        # 더미 없으면 첫 노드 뒤바뀌는것 생각 못했다. 더미 추가하기
        dummy = ListNode()
        dummy.next = head

        left_end = dummy
        start_node = head
        end_node = start_node
        while True:
            if k == 1: 
                break # 바꾸는 것 자체를 할 수 없다.

            sizecount = 1
            while sizecount < k and end_node.next is not None: # end node가 끝일때/ k 개 만큼 범위 지정됐을때 종료
                end_node = end_node.next
                sizecount += 1
            right_end = end_node.next
            
            if sizecount == k : #k > 1 개면 바꿔야 
                # swap1, swap2 = start_node, end_node  -> 단방향이라 swap 못함. 양 끝 이웃 노드만 기억하고, 방향만 바꾸기
                cur_node = start_node
                prev_node = left_end
                while cur_node is not right_end:
                    next_node = cur_node.next
                    cur_node.next = prev_node

                    prev_node = cur_node
                    cur_node = next_node

                start_node.next = right_end
                left_end.next = end_node

            if right_end is None: #  실패 : end_node는 의미가 바뀌었으므로, right_end로 비교해야 함  -> end_node라면, 항상 else - right end가 None이므로 위에서 NoneType has no attr. next 오류
                break
            else: 
                left_end = start_node # end_node 가 아님
                start_node = right_end
                end_node = start_node

        return dummy.next
            



        