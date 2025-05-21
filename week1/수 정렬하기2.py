import sys
input = sys.stdin.readline
n = int(input())
arr = [0]*n

for i in range(n):
    arr[i] = int(input())

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 1. 분할
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 2. 병합
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # 정렬하며 병합
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 요소 추가
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 예시
sorted_arr = merge_sort(arr)
for i in range(len(sorted_arr)):
    print(sorted_arr[i])
