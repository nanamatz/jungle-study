import sys
from collections import deque
input = sys.stdin.readline
V,E = map(int,input().split())

adj_list = [[] for _ in range(V+1)]
in_degree = [0] * (V+1)


for _ in range(E):
    u,v = map(int,input().split())
    adj_list[u].append(v)


for v in range(1,V+1):
    for u in adj_list[v]:
        in_degree[u] += 1

q = deque([i for i in range(1,V+1) if in_degree[i] == 0])
    
result = []
while q:
    node = q.popleft()
    print(node,end=" ")

    for neighbor in adj_list[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            q.append(neighbor)

