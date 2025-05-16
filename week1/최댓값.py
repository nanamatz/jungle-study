max = -1
cnt = 0
max_index = 0
for _ in range(9):
    temp = int(input())
    cnt += 1
    if max < temp:
        max = temp
        max_index = cnt

    
print(max)
print(max_index)