import sys
import heapq
input = sys.stdin.readline

n = int(input())

min_heap = []
prefix_sum = 0
for _ in range(n):
    heapq.heappush(min_heap,int(input()))

while(len(min_heap)>1):             #하나 남을 때까지 반복
    a = heapq.heappop(min_heap)
    b = heapq.heappop(min_heap)     
    result = a + b
    prefix_sum += result            #누적합을 계속 더 해준다.
    heapq.heappush(min_heap,result)

print(prefix_sum)