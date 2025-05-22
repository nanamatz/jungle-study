from itertools import combinations
n,s = map(int,input().split())

cnt = 0
arr = list(map(int,input().split()))
if n <= 1:
    if arr[0] == s:
        cnt += 1
else:
    for i in range(1,n+1):
        per_list = list(combinations(arr,i))
        for t in per_list:
            total = sum(t)
            if total == s:
                cnt += 1

print(cnt)



# for i in range(n):
#     p = 0
#     for j in range(i,n):
#         p += arr[j]