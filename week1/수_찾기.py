import BT

n = int(input())

keys = list(map(int,input().split()))

m = int(input())

arr = list(map(int,input().split()))

tree = BT.BinarySearchTree()

for i in range(n):
    tree.add(keys[i],None)

for i in range(m):
    if tree.search(arr[i]):
        print(1)
    else:
        print(0)










# def insert_bt(index,item):
#     if index >= 2**n:
#         return
    
#     if binary_tree[index] == None:
#         binary_tree[index] = item
#         return
#     elif binary_tree[index] < item:
#         index = index * 2 + 1
#     else:
#         index = index * 2
#     insert_bt(index,item)

# def binary_tree_search(index,key):
#     if index >= 2 ** n:
#         return print(0)
    
#     if binary_tree[index] == None:    #검색 실패
#         return print(0)
    
#     if binary_tree[index] < key:    #입력 값이 더 클 경우
#         index = (index * 2) + 1
#         return binary_tree_search(index,key)
    
#     elif binary_tree[index] == key: #입력 값과 동일할 경우
#         return print(1)
    
#     else:
#         index = index * 2
#         return binary_tree_search(index,key)    #입력 값 보다 작을 경우
# keys.sort()
# for i in range(n):
#     insert_bt(1,keys[i])

# for i in range(m):
#     binary_tree_search(1,arr[i])

