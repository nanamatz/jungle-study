import sys
input = sys.stdin.readline

n = int(input())
tower_list = list(map(int, input().split()))
stack = []
result = []

for i in range(n):
    current_height = tower_list[i]

    while stack and tower_list[stack[-1]] < current_height:
        stack.pop()

    if stack:
        result.append(stack[-1] + 1)
    else:
        result.append(0)

    stack.append(i)

print(*result)
