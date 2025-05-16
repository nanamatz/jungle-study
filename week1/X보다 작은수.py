n,x = list(map(int,input().split()))

arr = []
arr = list(map(int,input().split()))
for i in range(len(arr)):
    if x > arr[i]:
        print(f'{arr[i]} ',end="")
