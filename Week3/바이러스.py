from collections import deque
import sys
input = sys.stdin.readline

V = int(input())
E = int(input())

adj_list = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]

for _ in range(E):
    u,v = map(int,input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs():
    start = 1
    q = deque()
    visited[start] = True
    count = 0
    q.append(start)
    while(len(q)>0):
        u = q.popleft()
        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
                count += 1
    return count

print(bfs())

