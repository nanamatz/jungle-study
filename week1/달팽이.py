import math
a,b,v = list(map(int,input().split()))

k = v - a #도착점 - 순전진 거리 => 도착 직전 지점
distance = a-b # 일일 전진 거리
days = math.ceil(k/distance) + 1 #도착 직전 지점까지 걸리는 일 수를 구한 뒤 한 번 더 이동을 한다.
                                #(도착 직전 지점 상태일 때 기준 밤이므로 이동을 하는 낮으로 바뀌면서 하루가 추가된다.)
print(days)