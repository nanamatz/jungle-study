from collections import deque
n,m = map(int,input().split())

maze = []
q = deque()
adj_list = [[]for _ in range(n)]

for _ in range(n):
    path = input()
    nums = [int(ch) for ch in path]
    maze.append(nums)

def check(x,y):
    initial = len(q)
    if y + 1< m and maze[x][y+1] == 1:
        q.append((x,y+1))
        maze[x][y+1] += maze[x][y]

    if x + 1 < n and maze[x+1][y] == 1:
        q.append((x+1,y))
        maze[x+1][y] += maze[x][y]
                  
    if x - 1 >= 0 and maze[x-1][y] == 1:  #위 이동
        q.append((x-1,y))
        maze[x-1][y] += maze[x][y]

    if y - 1 >= 0 and maze[x][y-1] == 1:  #왼쪽 이동
        q.append((x,y-1))
        maze[x][y-1] += maze[x][y]

    if initial == len(q):
        return False
    return True
    
def bfs():
    startPos = (0,0)
    q.append(startPos)
    while(len(q)>0):
        Pos = q.popleft()
        x = Pos[0]
        y = Pos[1]
        if x == n-1 and y == m-1:
            return
        check(x,y)

bfs()
print(maze[n-1][m-1])

