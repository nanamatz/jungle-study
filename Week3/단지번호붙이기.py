import sys
from collections import deque

#input= sys.stdin.readline

N = int(input())

town_list = []
matrix = []*N

for _ in range(N):
    line = input()
    line = list(line)
    matrix.append([int(ch) for ch in line])

q = deque()

def check(x,y):

    if y+1 < N:
        if matrix[x][y+1] == 1:
            q.append((x,y+1))
            matrix[x][y+1] += radix

    if x+1 < N:
        if matrix[x+1][y] == 1:
            q.append((x+1,y))
            matrix[x+1][y] += radix

    if matrix[x][y-1] == 1 and y-1 >=0:
        q.append((x,y-1))
        matrix[x][y-1] += radix

    if matrix[x-1][y] == 1 and x-1 >= 0:
        q.append((x-1,y))
        matrix[x-1][y] += radix

radix = 1
def bfs(x,y):
    town_size = 0
    matrix[x][y] += radix
    q.append((x,y))
    while(q):
        pos = q.popleft()
        town_size += 1
        xPos = pos[0]
        yPos = pos[1]
        check(xPos,yPos)
    return town_size
    
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            town_list.append(bfs(i,j))
            radix += 1

print(len(town_list))
town_list.sort()

for size in town_list:
    print(size)
        