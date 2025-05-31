n = int(input())
apple = int(input())

turn_info_list = []
arr = [[0] * (n+2) for _ in range(n+2)]

def make_board():
    for i in range(n+2):
        for j in range(n+2):
            if i == 0 or i == n+1:
                arr[i][j] = -1
            elif j == 0 or j == n+1:
                arr[i][j] = -1

make_board()

for i in range(n+2):
    print(arr[i])

for _ in range(apple):
    x,y = int(input().split())
    arr[x][y] = 1

turn_cnt = int(input())
for _ in range(turn_cnt):
    time, direction = input().split()
    turn_info_list.append([int(time),direction])




