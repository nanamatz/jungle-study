n = int(input())


matrix = [[0] * n for _ in range(n)]

def print_mat():
    for i in range(n):
        for j in range(n):
            print(f'{matrix[i][j]:3}', end="")
        print()

for i in range(n):
    matrix[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if matrix[i][j] <= n:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 1

print_mat()
