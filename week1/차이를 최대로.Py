from itertools import permutations
n = int(input())

arr = list(map(int,input().split()))
max_gap = -1

def sum_gap(array: list) -> int:
    sum = 0
    for i in range(n-1):
        sum += abs(array[i] - array[i+1])
    return sum


for i in permutations(arr):             #모든 순열 찾아서 하나씩 결과값 찾는게 가능 n이 8까지라 최대 8!의 경우의 수만 확인하면 되기 때문에 쌉가능
    result = sum_gap(i)
    if result > max_gap:
        max_gap = result

print(max_gap)


# sum = 0
# for i in range(n-1):
#     sum += abs(arr[i] - arr[i+1])

# print(sum)
# print(arr)