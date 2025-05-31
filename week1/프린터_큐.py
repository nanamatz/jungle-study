import sys

input = sys.stdin.readline

T = int(input())

def how_many_big(target):
    cnt = 0
    last_big_index = 0
    for i in range(len(n_list)):
        if n_list[i] > target:
            last_big_index = i
    if last_big_index == 0:
        return cnt
    for j in range(last_big_index+1,len(n_list)):
        if n_list[j] == target:
            cnt+=1
    return cnt

for _ in range(T):
    n,m = map(int,input().split())
    n_list = list(map(int,input().split()))
    target = n_list[m]
    cnt = how_many_big(target)
    num = -1    

    while(len(n_list) > 0):
        if n_list[0] == max(n_list):
            num = n_list.pop(0)
            cnt+=1
            if num == target:
                print(cnt)
                break
        else:
            num = n_list.pop(0)
            n_list.append(num)


     


    