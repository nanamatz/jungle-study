import sys
input = sys.stdin.readline
n,m = map(int,input().split())

tree_list = list(map(int,input().split()))

left = 0
right = max(tree_list)
answer = 0

while(left<=right):
    result = 0

    mid = left + (right-left)//2

    h = mid
    result = sum(tree - mid for tree in tree_list if tree > mid)        #for문 보다 리스트 컴프리헨션이 연산이 빠르다. (오늘의 삽질 후기)
    #원래 반복문으로 짠 코드
    # for tree in tree_list:
    #     if tree > h:
    #         result += tree - h
    
    if result >= m:     #조건문 하나만 줄여도 연산 속도가 줄어든다.
        left = mid+1
        answer = mid
    #원래 작성했던 조건문
    # elif result == m:
    #     print(h)
    #     break
    else:
        right = mid-1
print(answer)


