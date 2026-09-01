class Node:
    def __init__(self, data): 
        self.value = data
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(None)
        self.capacity = capacity
        self.kvdict = {}
        self.head.next = self.head
        self.head.prev = self.head
    def get(self, key: int) -> int:  
        if self.kvdict.get(key) is None:
            return -1
        else:
            found_node = self.kvdict.get(key)
            # detach
            prev_node = found_node.prev
            next_node = found_node.next
            prev_node.next, next_node.prev = next_node, prev_node
            #insert --- head_next는 제거 끝난 뒤에 선언이 중요. 또한 나머지도 이전 선언 값과 섞이면 안됨 
            head_next = self.head.next
            self.head.next, head_next.prev, found_node.next, found_node.prev = found_node, found_node, head_next, self.head
            # self.head.next, self.head.next.prev, found_node.next, found_node.prev = found_node, found_node, self.headㅁ.next.prev, self.head -> 다중 대입은 하나씩 순서대로 수행하므로, rvalue가 capture되더라도, lvalue가 하나씩 수행되므로, 첫 번째 것이 대입된 후의 head.next는 다른 레퍼런스이다. 그러니 이렇게 하면 부적절
            return found_node.value[1]
        


    def put(self, key: int, value: int) -> None:# eviction이 연속할 수 있기 때문에 전체 사용 순서를 알고 있어야 한다
        to_remove = None
        if self.kvdict.get(key) is not None: # key가 있다면, capa 차도 해당 아이템 없애면 된다
            to_remove = self.kvdict[key]
        elif self.capacity == len(self.kvdict):
            to_remove = self.head.prev
        if to_remove is not None:
            self.kvdict.pop(to_remove.value[0])
            prev_node = to_remove.prev
            next_node = to_remove.next
            prev_node.next, next_node.prev = to_remove.next, to_remove.prev

        
        to_add = Node((key, value))
        head_next = self.head.next
        self.head.next, head_next.prev, to_add.next, to_add.prev = to_add, to_add, head_next, self.head

        self.kvdict[key] = to_add



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)