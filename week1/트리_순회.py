n = int(input())

class BinaryTree():
    def __init__(self,root):
        self.root = root

dic = {}

for i in range(n):
    key,left,right = input().split()
    dic[key] = (left,right)

def PreOrder(key):
    if key == '.':
        return
    print(key,end='')
    PreOrder(dic[key][0])
    PreOrder(dic[key][1])

def InOrder(key):
    if key == '.':
        return
    InOrder(dic[key][0])
    print(key,end='')
    InOrder(dic[key][1])

def PostOrder(key):
    if key == '.':
        return
    PostOrder(dic[key][0])
    PostOrder(dic[key][1])
    print(key,end='')
    
root = next(iter(dic))
PreOrder(root)
print()
InOrder(root)
print()
PostOrder(root)