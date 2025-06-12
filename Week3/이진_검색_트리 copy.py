n = int(input())

graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def dfs(x, y):
    global result
    if x < 0 or y < 0 or x >= n or y >= n:
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if graph[nx][ny] == 0:
            continue

        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            result += 1
            dfs(nx, ny)

count = 0
answer = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result = 1
            dfs(i, j)
            answer.append(result)
            count += 1

answer.sort()
print(count)

for i in range(count):
    print(answer[i])