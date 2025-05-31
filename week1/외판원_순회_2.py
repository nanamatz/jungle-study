n = int(input())
matrix = [[0]*n]*n

T = [False]* n
R = [0]*n

for i in range(n):
    for j in range(n):
        if (matrix[i][j] != 0 and T[j] == False):
            this_city = j
            T[this_city] = True
            

def print_matrix(matrix):
    for i in range(n):
        for j in range(n):
            print(f'{matrix[i][j]:3}',end="")
        print()

def init(matrix):
    for i in range(n):
        matrix[i] = list(map(int,input().split()))

init(matrix)
print_matrix(matrix)
