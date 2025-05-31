n = int(input())

class TreeNode():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.item = value

class BinaryTree():
    def __init__(self):
        self.root = None

def PreOrder(root):
    if root.item == None:
        return
    print(root.item,end='')
    PreOrder(root.left)
    PreOrder(root.right)

def InOrder(root):
    if root.item == None:
        return
    InOrder(root.left)
    print(root.item,end='')
    InOrder(root.right)

def PostOrder(root):
    if root.item == None:
        return
    PostOrder(root.left)
    PostOrder(root.right)
    print(root.item,end='')

def make_tree(root,item,left,right):
    if root.item == item:
        root.left = left
        root.right = right
        return
    make_tree(root.left,item,left,right)
    make_tree(root.right,item,left,right)

ele,lchild,rchild = map(str,input().split())

tree = BinaryTree()
tree.root = TreeNode(ele)

for _ in range(n-1):
    parent,left,right = map(str,input().split())
    make_tree(tree.root,parent,left,right)

PreOrder(tree.root)
InOrder(tree.root)
PostOrder(tree.root)
