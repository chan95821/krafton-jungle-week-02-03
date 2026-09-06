class Trie:
    class Node:
        def __init__(self, ch=None):
            self.val = ch
            self.children = {}

    def __init__(self):
        self.head = self.Node()

    def insert(self, word: str) -> None:
        current = self.head
        for ch in word:
            if ch in current.children:
                pass
            else:
                current.children[ch] = self.Node(ch)
            current = current.children[ch]
        current.children[-1] = self.Node()


    def search(self, word: str) -> bool:
        current = self.head
        for ch in word:
            if ch in current.children:
                current = current.children[ch]
            else: return False

        if -1 in current.children:
            return True
        else: return False


    def startsWith(self, prefix: str) -> bool:
        current = self.head
        for ch in prefix:
            if ch in current.children:
                current = current.children[ch]
            else: return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
