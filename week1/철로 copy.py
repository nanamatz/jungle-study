import sys
import heapq

input = sys.stdin.readline

n = int(input())

pos_list = []
for _ in range(n):
    pos_list.append(list(map(int,input().split())))

d = int(input())
events = []
for x,y in pos_list:
    if y > d:
        continue
    events.append((x,'start'))
    events.append((y,'end'))

events.sort()

active = 0
prev_x = 0
total_length = 0

for x, event in events:
    if active > 0:
        total_length += x - prev_x
    if event == 'start':
        active += 1
    else:
        active -= 1
    prev_x = x
    
print(total_length)
