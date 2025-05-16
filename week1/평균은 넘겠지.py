import sys
T = int(sys.stdin.readline())

for _ in range(T):
    class_list = list(map(int,sys.stdin.readline().split()))
    n = class_list.pop(0)
    score_sum = sum(class_list) # sum 변수명 조심
    avg = (score_sum//n) # /가 아닌 // 써야됨 안 그럼 런타임에러
    over_avg = 0
    for i in range(0,n):
        if class_list[i] > avg:
            over_avg += 1
    ratio = float(over_avg) / float(n) * 100
    round(ratio,4)
    print(f'{ratio:.3f}%')
