from collections import deque
import sys
input = sys.stdin.readline

V = int(input())

adj_list = [[]for _ in range(V+1)]

stack = deque()

visited = [False for _ in range(V+1)]
for _ in range(V-1):
    u,v = map(int,input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

parent_list = [-1 for _ in range(V+1)]
def dfs(start):
    visited[start] = 1
    stack.append(start)
    while(stack):
        u = stack.pop()
        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                parent_list[v] = u
                stack.append(v)

dfs(1)
[print(i) for i in parent_list[2:]]