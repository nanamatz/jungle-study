import sys
import heapq
input = sys.stdin.readline
def say_median(heap_size):

    length = (heap_size + 1 ) // 2      #전체 배열 크기의 절반 (두 개의 힙의 크기가 균형을 이루는 최대 크기)

    if length < len(max_heap):          #최대 크기보다 크면 편향되어 있는 거임
        temp = heapq.heappop(max_heap)  #조정해줌 max -> min
        heapq.heappush(min_heap,(-1)*temp)

    elif length < len(min_heap):        #똑같음
        temp = heapq.heappop(min_heap)  #조정해줌 Min -> max
        heapq.heappush(max_heap,(-1)*temp)

    median = 0

    if heap_size % 2 == 0:              #지금까지 힙의 원소 개수가 짝수면 두 힙의 루트를 비교해서 작은 값을 중앙값으로 함
        median = min((-1)*max_heap[0],min_heap[0])
    else:                               #홀수면 힙 사이즈가 1 차이날 것이므로 더 많은 원소의 루트가 중앙값이 됨
        if len(min_heap) < len(max_heap):
            median = (-1)*max_heap[0]
        else:
            median = min_heap[0]
        
    return median

n = int(sys.stdin.readline())

max_heap = []
min_heap = []
mid = 0

for i in range(n):

    num = int(input())

    if len(max_heap) == 0:              #초기 상태에서 무조건 Max 힙에 넣음
        heapq.heappush(max_heap,(-1)*num)
        print(say_median(i+1))
        continue
    elif len(min_heap) == 0:            #두 번째 원소가 들어오면 min에 넣지 않고 Mid 값만 설정해줌 어차피 median 계산할 때 조정됨.
        mid = (-1)*max_heap[0]
    else:
        mid = min_heap[0]

    if num <= mid:
        heapq.heappush(max_heap,num*(-1))
    else:
        heapq.heappush(min_heap,num)

    print(say_median(i+1))
