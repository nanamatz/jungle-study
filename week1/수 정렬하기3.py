import sys
input = sys.stdin.readline
n = int(input())

arr = [0] * 10001


for i in range(n):
    number = int(input())
    arr[number] += 1

for i in range(1,10001):
    if arr[i] != 0:
        for cnt in range(arr[i]):
            print(i)

    