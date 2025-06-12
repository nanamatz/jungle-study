#틀렸습니다 뜸

import sys

input = sys.stdin.readline

N,K = map(int,input().split())

matrix = [] * N

virus_order = [i for i in range(1,K+1)]

for _ in range(N):
    matrix.append(list(map(int,input().split())))


time,x,y = map(int,input().split())

def check(x,y,v):

    if y+1 < N:
        if matrix[x][y+1] == 0:
            matrix[x][y+1]=v

    if x+1 < N:
        if matrix[x+1][y] == 0:
            matrix[x+1][y]=v
            
    if matrix[x][y-1] == 0 and y-1 >=0:
            matrix[x][y-1]=v
        
    if matrix[x-1][y] == 0 and x-1 >= 0:
            matrix[x-1][y]=v


def bfs(x,y,v):
    check(x,y,v)
    

v = 1

for _ in range(time):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == v:
                bfs(i,j,v)
                v = (v + 1) % K
                if v == 0:
                    v = K

print(matrix[x-1][y-1])

