import numpy as np

n = int(input())
array = np.array([[1]*n]*n)
cnt = 0

def get_possible_index(level):
    for i in range(n):
        if array[level][i] == 1: #1일 경우
            return i
    return -1

def block_lines(x,y):
        for i in range(1,n):    #세로 블락
            array[i][y] = 0

        end = n - max(x,y)      #Index 바운더리를 최댓값에 따라 대각선 블락 횟수를 기준으로 잡는다. 

        for i in range(end):    #메인 대각선 (우하단) 블락                   
            array[x+i][y+i] = 0

        end = min(n-x-1,y) + 1  #Index 바운더리를 최소값에 따라 대각선 블락 횟수를 기준으로 잡는다.

        for i in range(end):      #서브 대각선 (좌하단) 블락
            array[x+i][y-i] = 0
             
        print(array)



def n_queen_put(level):
    if level == n:  # n개의 퀸을 다 놓았다면 리턴
        cnt += 1
        return
    i = get_possible_index(level)
    
    if i == -1: # 놓을 곳이 없을 때 리턴
        return
    
    array[level][i] = 0 #n행 i열에 퀸 놓기
    
    block_lines(level,i) #N행 i열을 기준으로 대각,직선 블락 처리
    
    level += 1 #일단 매개변수에 바로 안 넣고 변수에 따로 값 저장
    
    n_queen_put(level)
        

n_queen_put(n-n)
print(cnt)
        
    