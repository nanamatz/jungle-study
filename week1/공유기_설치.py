import sys
input = sys.stdin.readline
n,m = map(int,input().split())
pos = [0]*n
for i in range(n):
    pos[i] = int(input())

pos.sort()

low = 1
high = pos[n-1] - pos[0]

def is_possible(min_dist):
    cnt = 1
    last = pos[0]
    for cur in range(1,n):
        if pos[cur] - last >= min_dist:
            cnt += 1
            last = pos[cur]
    return cnt >= m

answer = 0

while(low <= high):
    mid = (high + low) // 2
    if is_possible(mid):
        answer = mid
        low = mid+1
    else:
        high = mid-1
    
print(answer)
    

