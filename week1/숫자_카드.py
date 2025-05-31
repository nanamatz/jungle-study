import sys
input = sys.stdin.readline

n = int(input())

n_heap = []
n_list = list(map(int,input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int,input().split()))

def find(num):
    low = 0
    high = n-1
    while(low <= high):
        mid = low + (high - low)//2
        if n_list[mid] == num:
            return 1
        elif n_list[mid] > num:
            high = mid - 1
        else:
            low = mid + 1
    return 0


for num in m_list:
    print(find(num),end=" ")