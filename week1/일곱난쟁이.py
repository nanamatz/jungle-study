arr = [0] * 9
for i in range(9):
    arr[i] = int(input())

arr.sort()
over = sum(arr)

x = over - 100
flag = False
for i in range(9):
    min = arr[i]
    for j in range(i,9):
        if (min + arr[j]) == x:
            value = arr[j]
            arr.remove(min)
            arr.remove(value)
            flag = True
            break
    if flag:
        break

for i in range(len(arr)):
    print(arr[i])

