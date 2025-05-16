a = int(input())
b = int(input())
c = int(input())

mult = a * b * c
arr = [0,0,0,0,0,0,0,0,0,0]
mult = str(mult)
for i in range(len(mult)):
    arr[int(mult[i])] += 1

for i in range(10):
    print(arr[i])