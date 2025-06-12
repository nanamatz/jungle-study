import sys
from collections import deque

#input = sys.stdin.readline
N,M = map(int,input().split())

adj_list = []*N

for _ in range(N):
    string = input()
    adj_list.append(list(string))

result = 0
for row in range(N):
    for col in range(M):
        if adj_list[row][col] == '-':
            if adj_list[row][col-1] == '-' and col-1 >= 0:
                continue
            else:
                result += 1
        else:
            if adj_list[row-1][col] == '|' and row - 1 >= 0:
                continue
            else:
                result += 1

print(result)