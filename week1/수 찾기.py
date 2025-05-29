n = int(input())

keys = list(map(int,input().split()))

m = int(input())

arr = list(map(int,input().split()))

keys.sort()

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # 인덱스를 반환
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # 찾지 못한 경우

for i in range(m):
    if binary_search(keys,arr[i]) == -1:
        print(0)
    else:
        print(1)