import sys
input = sys.stdin.readline
n = int(input())
solution_list = list(map(int,input().split()))

solution_list.sort()

#sort안하고 max,min으로만 하면 어떻게 될까?

answer = [0,0]

low = 0
high = n-1

best_fusion = 2000000001

while(low < high):

    standard = (solution_list[high]+solution_list[low])//2
    
    fusion = solution_list[low] + solution_list[high]
    
    if best_fusion >= abs(fusion):
        best_fusion = abs(fusion)
        answer[0] = low
        answer[1] = high

    if fusion > standard:
        high -= 1
    elif fusion < standard:
        low += 1
    else:
        if standard == 0:
            break
        elif standard < 0:
            low += 1
        else:
            high -= 1

print(solution_list[answer[0]],solution_list[answer[1]])


