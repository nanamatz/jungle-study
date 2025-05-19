a,b,c = int(input()),int(input()),int(input())

mult = a * b * c
arr = [0,0,0,0,0,0,0,0,0,0]
mult = str(mult)
for i in range(len(mult)):
    arr[int(mult[i])] += 1

for i in range(10):
    print(arr[i])