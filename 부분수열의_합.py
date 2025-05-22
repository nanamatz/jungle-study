n,s = map(int,input().split())

arr = list(map(int,input().split()))

total = sum(arr)

for i in range(n):
    p = 0
    for j in range(i,n):
        p += arr[j]