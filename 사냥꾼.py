m,n,l = map(int,input().split())

shoot_ranges = list(map(int,input().split()))

pos_list = []
shoot_ranges.sort()

for i in range(n):
    x,y = map(int,input().split())
    if y > l:
        continue
    pos_list.append([x,y])

def is_hunted(left,right):
    low = 0
    high = m - 1
    while(low <= high):
        mid = low + (high - low) // 2
        if left <= shoot_ranges[mid] <= right:
            return True
        elif shoot_ranges[mid] < left:  
            low = mid + 1
        else:
            high = mid - 1
    return False

count = 0

for pos in pos_list:
    x = pos[0]
    y = pos[1]
    left = x-(l-y)
    right = x+(l-y)
    if is_hunted(left,right):
        count += 1

print(count)
