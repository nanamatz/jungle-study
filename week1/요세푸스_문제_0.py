n,k = map(int,input().split())

nums = [i for i in range(1,n+1)]
temp = []
cur =-1
while(True):
    cnt = k
    while(cnt>0):
        cur = (cur + 1) % n
        cnt -= 1
        if nums[cur] == -1:
            cnt += 1
    temp.append(nums[cur])    
    nums[cur] = -1
    if sum(nums) == (-1 * n):
        break

print('<',end='')
for i in range(n):
    if i == n-1:
        print(temp[i],end='')
        break
    print(temp[i],end=', ')
print('>',end='')



        