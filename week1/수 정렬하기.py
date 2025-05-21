
n = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())
arr.sort()
for i in range(len(arr)):
    print(arr[i])