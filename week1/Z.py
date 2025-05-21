n,r,c = map(int,input().split())
arr = [[0 for col in range(2**n)]for row in range(2**n)]

def Z(n,arr,i,j,cnt,quad):
    if n == n:
        print(arr[r][c])
        return
    if quad > 4:
        return
    
    unit_d = 2 ** n
    #처음 ㄱㄱ
    arr[i][j] = cnt
    cnt += 1
    #열 이동
    j += unit_d
    arr[i][j] = cnt
    cnt += 1
    #대각 이동
    i += unit_d
    j -= unit_d
    arr[i][j] = cnt
    cnt +=1
    #열 이동
    j += unit_d
    arr[i][j] = cnt
    cnt+=1
    Z(n+1,arr,i,j,cnt)
    
    
    


def print_2d():
    for i in arr:
        for j in i:
            print(j,end="")
        print()

Z(n,arr,0,0,1,1)