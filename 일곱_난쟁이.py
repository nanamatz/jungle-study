arr = [0] * 9
for i in range(9):
    arr[i] = int(input())

arr.sort()
over = sum(arr)

x = over - 100

for i in range(9):
    min = arr[i]
    for j in range(i,9):
        if min + arr[j] == x:
            arr.remove(i)
            arr.remove(j)

print(arr)

