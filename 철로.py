import sys
import heapq

input = sys.stdin.readline

n = int(input())

def how_many_people():
    if len(pos_heap) == 0:
        return 0
    cnt = 0
    cnt_list = []
    pos = pos_heap[0]
    dx = pos[0]
    while(len(pos_heap) > 0):
        pos = heapq.heappop(pos_heap)
        x = pos[0]
        y = pos[1]
        if dx <= x and y <= dx + d:
            cnt += 1
        elif y > dx + d:
            dx = x
            cnt_list.append(cnt)
            cnt = 0
            continue
    return max(cnt_list)

pos_heap = []
pos_list = []

for _ in range(n):
    pos_list.append(list(map(int,input().split())))

d = int(input())

for pos in pos_list:
    if abs(pos[0] - pos[1]) > d:
        continue
    if pos[0] > pos[1]:
        pos[0],pos[1] = pos[1],pos[0]
    heapq.heappush(pos_heap,pos)

print(how_many_people())


# for pos in pos_heap:
#     if pre != pos[0]:
#         copy_heap = pos_heap.copy()
#         result.append(how_many_people(pos[0],copy_heap))
#         pre = pos[0]
