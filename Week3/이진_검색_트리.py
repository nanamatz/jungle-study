import sys
sys.setrecursionlimit(10**8) # 10^8 까지 늘림.
#시간 초과
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # 삽입 함수
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def postorder(self):
        self._postorder(self.root)
    
    def _postorder(self,node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.key)

tree = BST()

for line in sys.stdin:
    key = int(line)
    tree.insert(key)

tree.postorder()