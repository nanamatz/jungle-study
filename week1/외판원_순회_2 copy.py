n = int(input())
matrix = [[0]*n]*n

# dist = [[]*2]*n*(n-1)
# print(dist)

def print_matrix(matrix):
    for i in range(n):
        for j in range(n):
            print(f'{matrix[i][j]:3}',end="")
        print()

def init(matrix):
    for i in range(n):
        matrix[i] = list(map(int,input().split()))

def dp_shortest_path(matrix):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # if matrix[i][j] == 0 or matrix[i][k] == 0 or matrix[k][j] == 0:
                #     print(matrix[i][j], matrix[i][k],matrix[k][j])
                #     continue
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    print("***")
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    for i in range(n):
        for j in range(n):
            print(f'{matrix[i][j]:3}',end="")
        print()

init(matrix)
print_matrix(matrix)
print("==="*10)

dp_shortest_path(matrix)
print("==="*10)
