import sys
sys.setrecursionlimit(10**8)        #이거 안해주면 시간 초과남
n = int(input())
row = [-1]*n
d_list_1 = [-1]*(2*n-1) 
d_list_2 = [-1]*(2*n-1)
result = 0

def set(x,array,d1,d2,result):

    if x == n:      #마지막 행이 n-1까지 이므로 n번째 자식 함수에서 탈출한다. 그러면서 n개를 잘 놨으니까 +1
        result += 1
        return result,True

    for y in range(len(array)):
        if array[y] == -1:      #열 체크

            if d1[x-y+n-1] == -1:    #메인 대각선 체크(우하향)

                if d2[x+y] == -1:    #서브 대각선 체크(좌하향)
                    array[y] = y     #행과 대각선이 체크가 되면 put해준다.
                    d1[x-y+n-1] = 1 
                    d2[x+y] = 1

                    result,flag = set(x+1,array,d1,d2,result)   #자식들아 가라

                    if flag:
                        array[y] = -1     #자식 함수에서 적신호를 받으면 해당 함수에서 작업했던 것을 되돌린다.
                        d1[x-y+n-1] = -1  
                        d2[x+y] = -1
                        if y == n-1:    #열의 끝에 도달하면 상위 함수로 돌아간다.
                            return result,True
                else:
                    continue
            else:
                if y == n-1:    
                    return result,True
                continue
        else:
            if y == n-1:    
                return result,True
    return  result,False

result,flag = set(n-n,row,d_list_1,d_list_2,result)
print(result)
                
