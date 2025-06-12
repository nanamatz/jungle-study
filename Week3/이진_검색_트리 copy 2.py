import sys
sys.setrecursionlimit(10**6)

preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

def build_tree(start, end):
    if start >= end:
        return

    root = preorder[start]
    idx = start + 1

    while idx < end and preorder[idx] < root:
        idx += 1

    build_tree(start + 1, idx)
    build_tree(idx, end)
    print(root)

build_tree(0, len(preorder))
