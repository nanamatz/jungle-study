from collections import deque
n,m = map(int,input().split())

maze = []

pos_stack = deque()

for _ in range(n):
    path = input()
    nums = [int(ch) for ch in path]
    maze.append(nums)

def check(x,y):
    initial = len(pos_stack)

    if x - 1 >= 0:
        if maze[x-1][y] == 1:  #위 이동
            pos_stack.append((x-1,y))
    
    if y - 1 >= 0:
        if maze[x][y-1] == 1:  #왼쪽 이동
            pos_stack.append((x,y-1))

    if x + 1 < n : #아래 이동
        if maze[x+1][y] == 1:
            pos_stack.append((x+1,y))

    if y + 1< m :  #오른쪽 이동
        if maze[x][y+1] == 1:
            pos_stack.append((x,y+1))
    
    if len(pos_stack) == initial:
        return False

    return True

def escape_maze():
    count = 1
    x = 0
    y = 0
    maze[x][y] = 2
    
    while(x<=n and y<=m):
        if check(x,y):
            count += 1
        else:
            count -= 1
        
        pos = pos_stack.pop()

        x = pos[0]
        y = pos[1]
        
        maze[x][y] += 1
        
        if x == n-1 and y == m-1:
            return count

print(escape_maze())