import sys
input = sys.stdin.readline

V,E = map(int,input().split())

w_list = []

parent = [i for i in range(1,V+1)]

def find(x):
    if parent[x-1] == x:
        return x
    while(parent[x-1] != x):
        x = parent[x-1]
    return x

def union(a,b):
    r1 = find(a)
    r2 = find(b)
    parent[r1-1] = r2

for _ in range(E):
    u,v,w = map(int,input().split())
    data = (u,v,w)
    w_list.append(data)

cnt = 0
total = 0

w_list.sort(key= lambda x : x[1])

while(cnt < V - 1):
    edge = w_list.pop(0)
    u = edge[0]
    v = edge[1]
    w = edge[2]    

    if find(u) != find(v):
        union(u,v)
        total += w
        cnt += 1
print(total)