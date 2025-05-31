n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

visited = [False] * n
result = [] * n

def print_matrix(matrix):
    for i in range(n):
        for j in range(n):
            print(f'{matrix[i][j]:3}',end="")
        print()

def init(matrix):
    for i in range(n):
        matrix[i] = list(map(int,input().split()))

def find_shortest_path(i,visit_list):
    #starting point 저장해놨다가 마지막에 starting point에 대해서만 연산을 한다면?
    if i == n:
        return 0
    visit_list[i] = True

    for j in range(len(matrix[i])):
        if visit_list[j] == False and matrix[i][j] != 0:
            print(matrix[i][j] + find_shortest_path(j,visit_list))
    return find_shortest_path(i+1,visit_list)

init(matrix)
find_shortest_path(0,visited)
