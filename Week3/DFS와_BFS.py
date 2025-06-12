import sys
input = sys.stdin.readline
from collections import deque

V,E,start = map(int,input().split())

visited = [False for _ in range(V+1)]

adj_list = [[] for _ in range(V+1)]

def dfs(u):
    visited[u] = True
    print(u,end=' ')

    v = adj_list[u]

    for w in v:
        if not visited[w]:
            dfs(w)

def bfs(u):
    q = deque()

    visited[u] = True
    print(u,end=' ')
    q.append(u)

    while(len(q) != 0):
        v = q.popleft()
        v = adj_list[v]
        for w in v:
            if not visited[w]:
                print(w,end=' ')
                visited[w] = True
                q.append(w)

for _ in range(E):
    u,v = map(int,input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

for i in range(1,V+1):
    adj_list[i].sort()
    
dfs(start)
print()
for i in range(V+1):
    visited[i] = False
bfs(start)

