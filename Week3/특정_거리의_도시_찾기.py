import sys
from collections import deque

input = sys.stdin.readline

V,E,K,start = map(int,input().split())

adj_list = [[]for _ in range(V+1)]
dis_list = [-1 for _ in range(V+1)]


for _ in range(E):
    u,v = map(int,input().split())
    adj_list[u].append(v)

def bfs(start):
    dis_list[start] = 0
    
    q = deque()
    q.append(start)

    while(len(q)>0):
        u = q.popleft()

        for v in adj_list[u]:
            if dis_list[v] == -1:
                q.append(v)
                dis_list[v] = dis_list[u] + 1

bfs(start)

if not K in dis_list:
    print(-1)

[print(i) for i in range(len(dis_list)) if dis_list[i] == K]