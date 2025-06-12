import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
E = int(input())

adj_list = [[]for _ in range(V+1)]
dis_list = [-1 for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    adj_list[u].append((v,w))
    


start,end = map(int,input().split())


def bfs(start):
    q = deque()
    q.append(start)
    dis_list[start] = 0
    while(q):
        node = q.popleft()
        for v,w in adj_list[node]:
            if dis_list[v] == -1:
                dis_list[v] = dis_list[u] + w
                q.append(v)
            else:
                dis_list[v] = min(dis_list[v],dis_list[u]+w)

bfs(start)
print(dis_list[end])

