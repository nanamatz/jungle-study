from collections import deque
import sys
input = sys.stdin.readline

V,E = map(int,input().split())

visited = [False for _ in range(V+1)]

adj_list = [[] for _ in range(V+1)]

for _ in range(E):
    u,v = map(int,input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs(node):
    visited[node] = True
    q = deque()
    q.append(node)
    while(len(q)!=0):
        u = q.popleft()
        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

cnt = 0
for i in range(1,V+1):
    if not visited[i]:
        bfs(i)
        cnt+=1
    
            
print(cnt)


