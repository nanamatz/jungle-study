import sys
input = sys.stdin.readline

V,E = map(int,input().split())

edges = []

parent = [i for i in range(1,V+1)]
rank = [0] * V

def find(x):
    if parent[x-1] == x:
        return x
    while(parent[x-1] != x):
        x = parent[x-1]
    return x

# def find(x):
#     if parent[x-1] != x:
#         parent[x-1] = find(parent[x-1])  # 경로 압축
#     return parent[x-1]

def union(a,b):
    r1 = find(a)
    r2 = find(b)
    if r1 == r2:
        return
    if rank[r1-1] < rank[r2-1]:
        parent[r1-1] = r2
    else:
        parent[r2-1] = r1
        if rank[r1-1] == rank[r2-1]:
            rank[r1-1] += 1

for _ in range(E):
    u,v,w = map(int,input().split())
    data = (w,u,v)
    edges.append(data)

cnt = 0

edges.sort()
total = 0

while(cnt < V - 1):
    edge = edges.pop(0)
    w = edge[0]
    u = edge[1]
    v = edge[2]    

    if find(u) != find(v):
        union(u,v)
        total += w
        cnt += 1
print(total)