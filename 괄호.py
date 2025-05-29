from collections import deque
n = int(input())

stack = deque()

for _ in range(n):
    stack.clear()
    ps = input()
    is_vps = True
    for i in ps:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                is_vps = False
    if is_vps and len(stack) == 0:
        print("YES")
    else:
        print("NO")
