n = int(input())

matrix = [[0]*n]*n

visited = [[False] * n for _ in range(n)]

def print_matrix(matrix):
    for i in range(n):
        for j in range(n):
            print(f'{matrix[i][j]:3}',end="")
        print()

def init(matrix):
    for i in range(n):
        matrix[i] = list(map(int,input().split()))

# DFS 함수
def dfs(x, y):
    # 범위를 벗어나면 종료
    if x < 0 or x >= n or y < 0 or y >= n:
        return

    # 이미 방문했거나 이동 불가능한 곳이면 종료
    if visited[x][y] or matrix[x][y] == 0:
        dfs(x, y+1)

    visited[x][y] = True


# (0, 0) 위치부터 DFS 시작
init(matrix)
dfs(0, 0)

# 방문 결과 출력
for row in visited:
    print(row)
