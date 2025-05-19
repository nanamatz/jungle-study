n = int(input())
arr = list(map(int,input().split()))
count = 0
for i in range(len(arr)):
    if arr[i] == 1:
        continue
    flag = True

    for j in range(2,arr[i]): # 2~ 자기 자신-1 로 나누어 떨어지면 소수가 아님. 
        if arr[i] % j == 0:
            flag = False
            continue
    if flag: #한 번도 나누어 떨어지지 않았으면 소수이므로 +1
        count += 1
    
print(count)